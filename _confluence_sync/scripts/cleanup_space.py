#!/usr/bin/env python3
"""Clean up all folders from a Confluence space."""

import requests
from requests.auth import HTTPBasicAuth
import os
import time
import sys

def main():
    space_key = sys.argv[1] if len(sys.argv) > 1 else 'TEMPHUB'
    
    auth = HTTPBasicAuth('ramki@zeta.tech', os.environ['CONFLUENCE_TOKEN'])
    base_url = 'https://zeta-tm.atlassian.net'
    
    # Find all folders using CQL - delete as we go to avoid pagination issues
    cql = f'space = {space_key} AND type = folder'
    url = f'{base_url}/wiki/rest/api/content/search'
    
    all_folders = []
    seen_ids = set()  # Track folder IDs to avoid duplicates
    deleted_count = 0
    
    # Use a simpler approach: get batches and delete immediately
    # This avoids pagination issues and reduces memory usage
    max_iterations = 100  # Safety limit
    iteration = 0
    
    print("Finding and deleting folders...", flush=True)
    print(f"Space: {space_key}, URL: {url}", flush=True)
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n[Iteration {iteration}] Fetching batch...", flush=True)
        
        # Get next batch
        params = {'cql': cql, 'limit': 50}  # Smaller batches
        print(f"  Making request: {url} with params: {params}", flush=True)
        response = requests.get(url, params=params, auth=auth, timeout=30)
        print(f"  Response status: {response.status_code}", flush=True)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            break
        
        data = response.json()
        results = data.get('results', [])
        
        if not results:
            print("No more folders found.")
            break
        
        # Filter out already seen folders
        new_folders = []
        for folder in results:
            folder_id = folder.get('id')
            if folder_id and folder_id not in seen_ids:
                seen_ids.add(folder_id)
                new_folders.append(folder)
        
        if not new_folders:
            print(f"All folders in this batch were already processed. Total deleted: {deleted_count}")
            # If we're getting all duplicates, we're done
            break
        
        # Delete folders immediately
        for folder in new_folders:
            folder_id = folder.get('id')
            folder_title = folder.get('title', 'unknown')
            
            try:
                resp = requests.delete(f'{base_url}/wiki/rest/api/content/{folder_id}', auth=auth, timeout=10)
                if resp.status_code in [200, 204]:
                    deleted_count += 1
                    if deleted_count % 10 == 0:
                        print(f"Deleted {deleted_count} folders...")
                else:
                    print(f"  ⚠ Failed to delete {folder_title}: HTTP {resp.status_code}")
            except Exception as e:
                print(f"  ✗ Error deleting {folder_title}: {e}")
            
            time.sleep(0.1)  # Small delay to avoid rate limiting
        
        # If we got fewer results than requested, we're done
        if len(results) < 50:
            print("Reached end of results.")
            break
        
        time.sleep(0.5)  # Delay between batches
    
    if iteration >= max_iterations:
        print(f"⚠ Reached maximum iterations ({max_iterations}). Stopping to prevent infinite loop.")
    
    all_folders = list(seen_ids)  # For reporting
    
    print(f"\n=== Cleanup Complete ===")
    print(f"Total folders processed: {len(all_folders)}")
    print(f"Total folders deleted: {deleted_count}")

if __name__ == '__main__':
    main()
