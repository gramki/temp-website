/** Console inventory — canonical IDs from platform-developer-guide/pages/consoles/README.md */

export type ConsolePattern =
  | "landing"
  | "queue"
  | "list-detail"
  | "analytics"
  | "workflow"
  | "admin"
  | "resource";

export type ConsoleDefinition = {
  id: string;
  label: string;
  group: ConsoleGroupId;
  primaryQuestion: string;
  pattern: ConsolePattern;
};

export type ConsoleGroupId =
  | "work"
  | "workspaces"
  | "build"
  | "workforce"
  | "governance"
  | "resources"
  | "settings";

export type ConsoleGroup = {
  id: ConsoleGroupId;
  label: string;
  consoles: ConsoleDefinition[];
};

export const CONSOLE_GROUPS: ConsoleGroup[] = [
  {
    id: "work",
    label: "Work",
    consoles: [
      {
        id: "work-overview",
        label: "Work Overview",
        group: "work",
        primaryQuestion: "What needs attention now?",
        pattern: "landing"
      },
      {
        id: "orchestration",
        label: "Orchestration",
        group: "work",
        primaryQuestion: "What orchestration items exist and what is their status?",
        pattern: "list-detail"
      },
      {
        id: "progress",
        label: "Progress",
        group: "work",
        primaryQuestion: "How is work progressing across scopes?",
        pattern: "analytics"
      },
      {
        id: "work-rituals",
        label: "Rituals",
        group: "work",
        primaryQuestion: "What operating cadence rituals are active?",
        pattern: "workflow"
      },
      {
        id: "my-work",
        label: "My Work",
        group: "work",
        primaryQuestion: "What is assigned to me?",
        pattern: "landing"
      }
    ]
  },
  {
    id: "workspaces",
    label: "Workspaces",
    consoles: [
      {
        id: "workspaces-overview",
        label: "Workspaces Overview",
        group: "workspaces",
        primaryQuestion: "What is happening across all workspaces?",
        pattern: "landing"
      },
      {
        id: "workspace-infrastructure",
        label: "Infrastructure",
        group: "workspaces",
        primaryQuestion: "What pods are running and where are they scheduled?",
        pattern: "resource"
      },
      {
        id: "workspace-agents",
        label: "Agents",
        group: "workspaces",
        primaryQuestion: "How are agents, skills, and tokens used across this workbench?",
        pattern: "analytics"
      }
    ]
  },
  {
    id: "build",
    label: "Build",
    consoles: [
      {
        id: "ci",
        label: "CI Console",
        group: "build",
        primaryQuestion: "What is the build and pipeline status?",
        pattern: "queue"
      },
      {
        id: "components",
        label: "Components Console",
        group: "build",
        primaryQuestion: "What systems and components exist?",
        pattern: "list-detail"
      },
      {
        id: "findings",
        label: "Findings Console",
        group: "build",
        primaryQuestion: "What build findings need attention?",
        pattern: "queue"
      },
      {
        id: "quality-status",
        label: "Quality Status",
        group: "build",
        primaryQuestion: "What are test results and coverage trends?",
        pattern: "analytics"
      },
      {
        id: "release-artifacts",
        label: "Release Artifacts",
        group: "build",
        primaryQuestion: "What release artifacts exist and what is their status?",
        pattern: "list-detail"
      }
    ]
  },
  {
    id: "workforce",
    label: "Workforce",
    consoles: [
      {
        id: "workforce-overview",
        label: "Workforce Overview",
        group: "workforce",
        primaryQuestion: "Who and what is doing the work?",
        pattern: "landing"
      },
      {
        id: "team",
        label: "Team Console",
        group: "workforce",
        primaryQuestion: "Who is on the team and what is their capacity?",
        pattern: "list-detail"
      },
      {
        id: "agent",
        label: "Agent Console",
        group: "workforce",
        primaryQuestion: "What agents are employed and how are they performing?",
        pattern: "list-detail"
      }
    ]
  },
  {
    id: "governance",
    label: "Governance",
    consoles: [
      {
        id: "governance",
        label: "Governance Overview",
        group: "governance",
        primaryQuestion: "Is the work system healthy and controlled?",
        pattern: "landing"
      },
      {
        id: "rituals",
        label: "Rituals",
        group: "governance",
        primaryQuestion: "What governance rituals are scheduled or due?",
        pattern: "workflow"
      },
      {
        id: "controls",
        label: "Controls & Enforcement",
        group: "governance",
        primaryQuestion: "Are controls enforced and within thresholds?",
        pattern: "list-detail"
      },
      {
        id: "registers",
        label: "Registers",
        group: "governance",
        primaryQuestion: "What risks, debt, and exceptions are registered?",
        pattern: "queue"
      },
      {
        id: "reports",
        label: "Reports & Dashboards",
        group: "governance",
        primaryQuestion: "What governance reports and dashboards are available?",
        pattern: "analytics"
      },
      {
        id: "quality-compliance",
        label: "Quality Controls",
        group: "governance",
        primaryQuestion: "Do build and release quality controls pass thresholds?",
        pattern: "list-detail"
      }
    ]
  },
  {
    id: "resources",
    label: "Resources",
    consoles: [
      {
        id: "repositories",
        label: "Repositories & Tools",
        group: "resources",
        primaryQuestion: "Where are repositories and external tools?",
        pattern: "resource"
      }
    ]
  },
  {
    id: "settings",
    label: "Settings",
    consoles: [
      {
        id: "admin",
        label: "Admin Console",
        group: "settings",
        primaryQuestion: "How is the workbench configured?",
        pattern: "admin"
      },
      {
        id: "governance-admin",
        label: "Governance Admin",
        group: "settings",
        primaryQuestion: "How is governance authority and policy configured?",
        pattern: "admin"
      }
    ]
  }
];

export function getConsoleById(consoleId: string): ConsoleDefinition | undefined {
  for (const group of CONSOLE_GROUPS) {
    const found = group.consoles.find((c) => c.id === consoleId);
    if (found) {
      return found;
    }
  }
  return undefined;
}

export function getAllConsoleIds(): string[] {
  return CONSOLE_GROUPS.flatMap((g) => g.consoles.map((c) => c.id));
}
