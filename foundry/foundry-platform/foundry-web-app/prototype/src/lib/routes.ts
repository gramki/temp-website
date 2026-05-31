/** Canonical route helpers — see platform-developer-guide/pages/README.md */

export const DEFAULT_WORKSHOP_ID = "ws-photon";
export const DEFAULT_WORKBENCH_ID = "wb-photon-payment-gateway";

export function foundryHomePath(): string {
  return "/";
}

export function workshopHomePath(workshopId: string): string {
  return `/workshops/${workshopId}`;
}

export function workbenchHomePath(workbenchId: string): string {
  return `/workbenches/${workbenchId}`;
}

export function consolePath(workbenchId: string, consoleId: string): string {
  return `/workbenches/${workbenchId}/consoles/${consoleId}`;
}

export function orchestrationItemPath(
  workbenchId: string,
  type: string,
  itemId: string
): string {
  return `/workbenches/${workbenchId}/orchestration/${type}/${itemId}`;
}

export function teamMemberPath(workbenchId: string, memberId: string): string {
  return `/workbenches/${workbenchId}/team/${memberId}`;
}

export function workspaceSessionPath(
  workbenchId: string,
  sessionId: string
): string {
  return `/workbenches/${workbenchId}/sessions/${sessionId}`;
}

export function workOrderDetailPath(
  workbenchId: string,
  workOrderId: string
): string {
  return `/workbenches/${workbenchId}/work-orders/${workOrderId}`;
}
