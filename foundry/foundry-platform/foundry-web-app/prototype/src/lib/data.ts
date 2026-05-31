import currentUserData from "../../mock-data/current-user.json";
import activityEventsData from "../../mock-data/activity-events.json";
import coderPodsData from "../../mock-data/coder-pods.json";
import releaseIntentsData from "../../mock-data/release-intents.json";
import scenarioData from "../../mock-data/scenarios/buildTrackTwoWorkOrders.json";
import discoveryCasesData from "../../mock-data/discovery-cases.json";
import governanceData from "../../mock-data/governance-verdicts.json";
import productIntentsData from "../../mock-data/product-intents.json";
import sessionActivityEventsData from "../../mock-data/session-activity-events.json";
import sessionEmployedAgentsData from "../../mock-data/session-employed-agents.json";
import sessionTokenUsageData from "../../mock-data/session-token-usage.json";
import tasksData from "../../mock-data/tasks.json";
import teamMemberProfilesData from "../../mock-data/team-member-profiles.json";
import teamsData from "../../mock-data/teams.json";
import traceabilityData from "../../mock-data/traceability-links.json";
import workbenchesData from "../../mock-data/workbenches.json";
import workOrdersData from "../../mock-data/work-orders.json";
import workshopsData from "../../mock-data/workshops.json";
import workspaceSessionsData from "../../mock-data/workspace-sessions.json";

export const scenario = scenarioData;
export const tenant = workshopsData.tenant;
export const currentUser = currentUserData.currentUser;
export const workshops = workshopsData.workshops;
export const workbenches = workbenchesData.workbenches;
export const discoveryCases = discoveryCasesData.discoveryCases;
export const productIntents = productIntentsData.productIntents;
export const workOrders = workOrdersData.workOrders;
export const tasks = tasksData.tasks;
export const governanceVerdicts = governanceData.governanceVerdicts;
export const traceabilityLinks = traceabilityData.traceabilityLinks;
export const teams = teamsData;
export const activityEvents = activityEventsData.activityEvents;
export const releaseIntents = releaseIntentsData.releaseIntents;
export const workspaceSessions = workspaceSessionsData.workspaceSessions;
export const sessionActivityEventTypes = sessionActivityEventsData.eventTypes;
export const sessionActivityEvents = sessionActivityEventsData.sessionActivityEvents;
export const sessionCoderPods = coderPodsData.sessionCoderPods;
export const sessionAgentUsageWindows = sessionEmployedAgentsData.usageWindows;
export const sessionEmployedAgents = sessionEmployedAgentsData.sessionEmployedAgents;
export const sessionTokenUsage = sessionTokenUsageData.sessionTokenUsage;
export const teamMemberProfiles = teamMemberProfilesData.teamMemberProfiles;

type WorkspaceSessionWorkOrderOwnershipViolation = {
  sessionId: string;
  workOrderId: string;
  sessionOwnerId: string;
  workOrderOwner: string;
};

const workOrdersById = new Map(workOrders.map((workOrder) => [workOrder.id, workOrder]));
const workOrderOwnerByWorkspaceSessionOwner = new Map<string, string>();

const workspaceSessionWorkOrderOwnershipViolations: WorkspaceSessionWorkOrderOwnershipViolation[] =
  workspaceSessions.flatMap((session) =>
    session.workOrderIds.flatMap((workOrderId) => {
      const linkedWorkOrder = workOrdersById.get(workOrderId);
      if (!linkedWorkOrder) {
        return [];
      }
      const existingOwner = workOrderOwnerByWorkspaceSessionOwner.get(workOrderId);
      const normalizedOwner = existingOwner ?? session.ownerId;
      if (!existingOwner) {
        workOrderOwnerByWorkspaceSessionOwner.set(workOrderId, normalizedOwner);
      }
      if (
        linkedWorkOrder.owner !== session.ownerId ||
        normalizedOwner !== session.ownerId
      ) {
        return [
          {
            sessionId: session.id,
            workOrderId,
            sessionOwnerId: session.ownerId,
            workOrderOwner: linkedWorkOrder.owner
          }
        ];
      }
      return [];
    })
  );

export function getWorkshop(workshopId: string) {
  return workshops.find((w) => w.id === workshopId);
}

export function getWorkbench(workbenchId: string) {
  return workbenches.find((w) => w.id === workbenchId);
}

export function getProductIntent(intentId: string) {
  return productIntents.find((pi) => pi.id === intentId);
}

export function getDiscoveryCase(caseId: string) {
  return discoveryCases.find((dc) => dc.id === caseId);
}

export function getWorkOrder(workOrderId: string) {
  return workOrders.find((wo) => wo.id === workOrderId);
}

export function getWorkspaceSessionOwnedWorkOrders(sessionId: string) {
  const session = getWorkspaceSession(sessionId);
  if (!session) {
    return [];
  }
  const linkedWorkOrders = session.workOrderIds
    .map((workOrderId) => workOrdersById.get(workOrderId))
    .filter((workOrder): workOrder is NonNullable<typeof workOrder> => Boolean(workOrder));
  return linkedWorkOrders.filter((workOrder) => workOrder.owner === session.ownerId);
}

export function getWorkspaceSessionWorkOrderOwner(workOrderId: string) {
  return workOrderOwnerByWorkspaceSessionOwner.get(workOrderId);
}

export function getWorkspaceSessionWorkOrderOwnershipViolations() {
  return [...workspaceSessionWorkOrderOwnershipViolations];
}

export function getTasksForWorkOrder(workOrderId: string) {
  return tasks.filter((t) => t.workOrderId === workOrderId);
}

export function getGovernanceForIntent(intentId: string) {
  const linkIds = traceabilityLinks
    .filter(
      (l) =>
        l.type === "product-intent-to-governance-verdict" &&
        l.sourceId === intentId
    )
    .map((l) => l.targetId);
  return governanceVerdicts.filter((gv) => linkIds.includes(gv.id));
}

export function getWorkOrdersForIntent(intentId: string) {
  return workOrders.filter((wo) => wo.orchestrationItemId === intentId);
}

export function getWorkbenchTeam(workbenchId: string) {
  return teams.workbenchTeams.find((t) => t.workbenchId === workbenchId);
}

export function getReleaseIntent(releaseIntentId: string) {
  return releaseIntents.find((ri) => ri.id === releaseIntentId);
}

export function getReleaseIntentsForWorkbench(workbenchId: string) {
  return releaseIntents.filter((ri) => ri.workbenchId === workbenchId);
}

export function getWorkspaceSession(sessionId: string) {
  return workspaceSessions.find((session) => session.id === sessionId);
}

export function getWorkspaceSessionsForWorkbench(workbenchId: string) {
  return workspaceSessions
    .filter((session) => session.workbenchId === workbenchId)
    .sort(
      (a, b) =>
        new Date(b.lastUpdatedAt).getTime() - new Date(a.lastUpdatedAt).getTime()
    );
}

export function getWorkspaceSessionsForType(
  workbenchId: string,
  workspaceType: string
) {
  return getWorkspaceSessionsForWorkbench(workbenchId).filter(
    (session) => session.workspaceType === workspaceType
  );
}

export function getSessionActivityEventTypes() {
  return [...sessionActivityEventTypes];
}

export function getSessionActivity(
  sessionId: string,
  options?: {
    eventTypes?: string[];
    limit?: number;
  }
) {
  const selectedTypes =
    options?.eventTypes && options.eventTypes.length > 0
      ? new Set(options.eventTypes)
      : undefined;

  const sorted = sessionActivityEvents
    .filter((event) => event.sessionId === sessionId)
    .filter((event) => !selectedTypes || selectedTypes.has(event.eventType))
    .sort(
      (a, b) => new Date(b.occurredAt).getTime() - new Date(a.occurredAt).getTime()
    );

  return typeof options?.limit === "number" ? sorted.slice(0, options.limit) : sorted;
}

export function getSessionCoderPod(sessionId: string) {
  return sessionCoderPods.find((item) => item.sessionId === sessionId);
}

export function getSessionEmployedAgents(sessionId: string) {
  return sessionEmployedAgents.find((item) => item.sessionId === sessionId);
}

export type AgentUsageLogEntry = {
  agentId: string;
  agentName: string;
  sessionId: string;
  sessionTitle: string;
  workbenchId: string;
  ownerId: string;
  from: string;
  to: string;
  invocationCount: number;
  skills: {
    skillId: string;
    skillName: string;
    invocationCount: number;
  }[];
};

export function getAgentUsageLog(agentId: string) {
  const usageEntries: AgentUsageLogEntry[] = [];

  for (const sessionUsage of sessionEmployedAgents) {
    const allWindow = sessionUsage.windows.all;
    const session = getWorkspaceSession(sessionUsage.sessionId);
    if (!allWindow || !session) {
      continue;
    }

    const matchingAgent = allWindow.agents.find((agent) => agent.agentId === agentId);
    if (!matchingAgent) {
      continue;
    }

    usageEntries.push({
      agentId: matchingAgent.agentId,
      agentName: matchingAgent.agentName,
      sessionId: session.id,
      sessionTitle: session.title,
      workbenchId: session.workbenchId,
      ownerId: session.ownerId,
      from: allWindow.from,
      to: allWindow.to,
      invocationCount: matchingAgent.invocationCount,
      skills: matchingAgent.skills.map((skill) => ({ ...skill }))
    });
  }

  return usageEntries.sort(
    (a, b) => new Date(b.to).getTime() - new Date(a.to).getTime()
  );
}

export function getSessionAgentUsage(windowId: string, sessionId: string) {
  const employedAgents = getSessionEmployedAgents(sessionId);
  if (!employedAgents) {
    return undefined;
  }
  const windows = employedAgents.windows;
  const selectedWindow =
    windows[windowId as keyof typeof windows] ?? windows.all;
  return selectedWindow;
}

export function getSessionAgentWindows() {
  return [...sessionAgentUsageWindows];
}

export function getSessionTokenUsage(sessionId: string) {
  return sessionTokenUsage.find((item) => item.sessionId === sessionId);
}

export function getSessionTokenUsageTotals(sessionId: string) {
  const usage = getSessionTokenUsage(sessionId);
  return usage?.totals;
}

export function getActivityForWorkbench(workbenchId: string, limit?: number) {
  const sorted = activityEvents
    .filter((event) => event.workbenchId === workbenchId)
    .sort(
      (a, b) => new Date(b.occurredAt).getTime() - new Date(a.occurredAt).getTime()
    );
  return typeof limit === "number" ? sorted.slice(0, limit) : sorted;
}

export function getActivityByIds(activityIds: string[]) {
  const idSet = new Set(activityIds);
  return activityEvents
    .filter((event) => idSet.has(event.id))
    .sort(
      (a, b) => new Date(b.occurredAt).getTime() - new Date(a.occurredAt).getTime()
    );
}

export function getTeamMemberProfile(memberId: string) {
  return teamMemberProfiles.find((profile) => profile.memberId === memberId);
}

export function getIntentsForWorkbench(workbenchId: string) {
  return productIntents.filter((pi) => pi.workbenchId === workbenchId);
}

export function getWorkOrdersForWorkbench(workbenchId: string) {
  return workOrders.filter((wo) => wo.workbenchId === workbenchId);
}

export function getPrioritizedWorkOrders() {
  return scenario.prioritizedWorkOrderIds
    .map((id) => getWorkOrder(id))
    .filter((wo): wo is NonNullable<typeof wo> => Boolean(wo));
}

export function getScenarioIntent() {
  return getProductIntent(scenario.selectedProductIntentId);
}

export function resolvePersonName(personId: string): string {
  for (const team of teams.workbenchTeams) {
    const all = [
      ...team.productManagers,
      ...team.developers,
      ...team.qaPeople
    ];
    const found = all.find((p) => p.id === personId);
    if (found) {
      return found.name;
    }
  }
  for (const ws of Object.values(teams.workshopSharedRoles)) {
    const all = [...ws.releaseManagers, ...ws.uxPeople];
    const found = all.find((p) => p.id === personId);
    if (found) {
      return found.name;
    }
  }
  return personId;
}
