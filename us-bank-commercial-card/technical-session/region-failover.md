
## Region Failover Procedure
1. Confirm which services are inaccessible (Assume full-region unavailability)
2. Verify that Admin space is accessible for the Zone; If not follow the Admin Space Migration procedure
3. Confirm the list of Application Clusters and Database Clusters that need to move to the Green Zone
4. Initiate Blue->Green Migration producedure for the DB Clusters
5. Verify the DNS-based accessibility of the Database Clusters
6. Initiate the Blue->Green mirgation procedure for th eApplication Clusters
7. Verify the traffic flows are restored



## Admin Space Migration
1. Restore Atlantis Control Plane in the Green Region
2. Switchover the Admin DB Cluster to the Green Region
3. Verify that SRE Home, Weave CDM, Elenchos services are responding appropriately
