import { useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { ConsolePage } from "@/foundry-ui/components/ConsolePage";
import { Breadcrumb } from "@/foundry-ui/components/ConsolePage";
import { StatusBadge } from "@/foundry-ui/components";
import { BuildTrackPanel } from "@/features/build/BuildTrackPanel";
import {
  getActivityByIds,
  discoveryCases,
  getGovernanceForIntent,
  getActivityForWorkbench,
  getIntentsForWorkbench,
  getPrioritizedWorkOrders,
  getProductIntent,
  getReleaseIntent,
  getReleaseIntentsForWorkbench,
  getDiscoveryCase,
  getSessionActivity,
  getSessionActivityEventTypes,
  getAgentUsageLog,
  getSessionAgentUsage,
  getSessionAgentWindows,
  getSessionCoderPod,
  getSessionEmployedAgents,
  getSessionTokenUsage,
  getTeamMemberProfile,
  getWorkOrder,
  getWorkbench,
  getWorkbenchTeam,
  getWorkshop,
  getWorkspaceSession,
  getWorkspaceSessionOwnedWorkOrders,
  getWorkspaceSessionsForWorkbench,
  getWorkOrdersForWorkbench,
  governanceVerdicts,
  resolvePersonName,
  scenario
} from "@/lib/data";
import { getConsoleById } from "@/lib/navigation";
import {
  consolePath,
  foundryHomePath,
  orchestrationItemPath,
  teamMemberPath,
  workOrderDetailPath,
  workbenchHomePath,
  workshopHomePath,
  workspaceSessionPath
} from "@/lib/routes";

function GenericPlaceholder({ label }: { label: string }) {
  return (
    <div className="f-card">
      <p>{label} — prototype baseline surface. Data-driven depth added per journey.</p>
      <StatusBadge tone="info">Ready</StatusBadge>
    </div>
  );
}

function formatDateTime(isoTs: string) {
  return new Date(isoTs).toLocaleString("en-IN", {
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function formatDuration(minutes: number) {
  const safeMinutes = Math.max(0, minutes);
  const hours = Math.floor(safeMinutes / 60);
  const mins = safeMinutes % 60;
  if (hours === 0) {
    return `${mins}m`;
  }
  if (mins === 0) {
    return `${hours}h`;
  }
  return `${hours}h ${mins}m`;
}

function getElapsedWorkOrderMinutesInSession(
  workOrder: { createdAt: string; updatedAt: string },
  session: { startedAt: string; lastUpdatedAt: string }
) {
  const sessionStart = new Date(session.startedAt).getTime();
  const sessionEnd = new Date(session.lastUpdatedAt).getTime();
  const workOrderStart = new Date(workOrder.createdAt).getTime();
  const workOrderEnd = new Date(workOrder.updatedAt).getTime();
  const overlapStart = Math.max(sessionStart, workOrderStart);
  const overlapEnd = Math.min(sessionEnd, workOrderEnd);

  if (overlapEnd <= overlapStart) {
    return 0;
  }

  return Math.round((overlapEnd - overlapStart) / (60 * 1000));
}

function formatCurrencyUsd(amount: number) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  }).format(amount);
}

function formatTokenCount(tokens: number) {
  return new Intl.NumberFormat("en-IN").format(tokens);
}

function formatCompactTokenCount(tokens: number) {
  return new Intl.NumberFormat("en-IN", {
    notation: "compact",
    maximumFractionDigits: 1
  }).format(tokens);
}

function formatPercent(value: number) {
  return `${value.toFixed(1)}%`;
}

function initialsForName(name: string) {
  return name
    .split(" ")
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0]?.toUpperCase() ?? "")
    .join("");
}

function formatLogTimestamp(isoTs: string) {
  return new Date(isoTs).toISOString();
}

type TokenDailyPoint = {
  date: string;
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  cacheWriteTokens: number;
  totalTokens: number;
  totalCostUsd: number;
};

const WORKSPACE_TYPE_ORDER = [
  "product-spec",
  "ux-design",
  "development",
  "qa",
  "release",
  "governance"
] as const;

function workspaceTypeLabel(workspaceType: string) {
  const labels: Record<string, string> = {
    "product-spec": "Product Specification",
    "ux-design": "UX Design",
    development: "Development",
    qa: "QA",
    release: "Release",
    governance: "Governance"
  };
  return labels[workspaceType] ?? workspaceType;
}

function workspaceTypeIcon(workspaceType: string) {
  const icons: Record<string, string> = {
    "product-spec": "📘",
    "ux-design": "🎨",
    development: "🛠",
    qa: "🧪",
    release: "🚀",
    governance: "🛡"
  };
  return icons[workspaceType] ?? "📁";
}

const SESSION_ICON = "🖥";

function TokenUsageTimeline({
  daily
}: {
  daily: TokenDailyPoint[];
}) {
  if (daily.length === 0) {
    return <p className="f-meta-line">No token timeline data for this session.</p>;
  }

  const maxTotal = Math.max(...daily.map((point) => point.totalTokens), 1);

  return (
    <div className="f-token-chart">
      <div className="f-token-chart-bars" role="img" aria-label="Tokens per day chart">
        {daily.map((point) => {
          const inputHeight = (point.inputTokens / maxTotal) * 100;
          const outputHeight = (point.outputTokens / maxTotal) * 100;
          const cacheReadHeight = (point.cacheReadTokens / maxTotal) * 100;
          const cacheWriteHeight = (point.cacheWriteTokens / maxTotal) * 100;
          const dayLabel = new Date(point.date).toLocaleDateString("en-IN", {
            month: "short",
            day: "numeric"
          });

          return (
            <div
              key={point.date}
              className="f-token-chart-day"
              title={`${dayLabel}: ${formatTokenCount(point.totalTokens)} tokens • ${formatCurrencyUsd(
                point.totalCostUsd
              )}`}
            >
              <div className="f-token-chart-column">
                <span
                  className="f-token-chart-segment f-token-chart-segment--cache-write"
                  style={{ height: `${cacheWriteHeight}%` }}
                />
                <span
                  className="f-token-chart-segment f-token-chart-segment--cache-read"
                  style={{ height: `${cacheReadHeight}%` }}
                />
                <span
                  className="f-token-chart-segment f-token-chart-segment--output"
                  style={{ height: `${outputHeight}%` }}
                />
                <span
                  className="f-token-chart-segment f-token-chart-segment--input"
                  style={{ height: `${inputHeight}%` }}
                />
              </div>
              <p className="f-token-chart-day-label">{dayLabel}</p>
            </div>
          );
        })}
      </div>
      <div className="f-token-chart-legend">
        <span className="f-token-legend-item">
          <i className="f-token-legend-dot f-token-chart-segment--input" /> Input
        </span>
        <span className="f-token-legend-item">
          <i className="f-token-legend-dot f-token-chart-segment--output" /> Output
        </span>
        <span className="f-token-legend-item">
          <i className="f-token-legend-dot f-token-chart-segment--cache-read" /> Cache read
        </span>
        <span className="f-token-legend-item">
          <i className="f-token-legend-dot f-token-chart-segment--cache-write" /> Cache write
        </span>
      </div>
    </div>
  );
}

function TokenCostBars({
  items,
  title
}: {
  items: Array<{
    id: string;
    label: string;
    totalCostUsd: number;
    detail: string;
    secondaryDetail?: string;
  }>;
  title: string;
}) {
  const maxCost = Math.max(...items.map((item) => item.totalCostUsd), 1);

  return (
    <section className="f-card f-card--nested">
      <h4 className="f-subtitle">{title}</h4>
      <ul className="f-list f-list--plain f-token-breakdown-list">
        {items.map((item) => {
          const widthPercent = Math.max(6, (item.totalCostUsd / maxCost) * 100);
          return (
            <li key={item.id} className="f-token-breakdown-item">
              <div className="f-token-breakdown-head">
                <p className="f-tech">{item.label}</p>
                <p className="f-tech">{formatCurrencyUsd(item.totalCostUsd)}</p>
              </div>
              <div className="f-token-breakdown-track" aria-hidden="true">
                <div
                  className="f-token-breakdown-fill"
                  style={{ width: `${Math.min(100, widthPercent)}%` }}
                />
              </div>
              <p className="f-meta-line">{item.detail}</p>
              {item.secondaryDetail ? (
                <p className="f-meta-line">{item.secondaryDetail}</p>
              ) : null}
            </li>
          );
        })}
      </ul>
    </section>
  );
}

type WorkbenchAgentsTab = "overview" | "models" | "daily" | "agents";

function WorkbenchAgentsConsole({ workbenchId }: { workbenchId: string }) {
  const windows = getSessionAgentWindows();
  const [selectedWindow, setSelectedWindow] = useState(windows[0]?.id ?? "all");
  const [activeTab, setActiveTab] = useState<WorkbenchAgentsTab>("overview");
  const sessions = getWorkspaceSessionsForWorkbench(workbenchId);

  const aggregated = useMemo(() => {
    const agentUsageMap = new Map<
      string,
      {
        agentName: string;
        invocationCount: number;
        skills: Map<string, { skillName: string; invocationCount: number }>;
        sessionLogs: {
          sessionId: string;
          sessionTitle: string;
          ownerId: string;
          from: string;
          to: string;
          invocationCount: number;
          skills: { skillId: string; skillName: string; invocationCount: number }[];
        }[];
      }
    >();
    const skillTotals = new Map<string, { skillName: string; invocationCount: number }>();
    const modelTotals = new Map<
      string,
      {
        modelId: string;
        inputTokens: number;
        outputTokens: number;
        cacheReadTokens: number;
        cacheWriteTokens: number;
        totalCostUsd: number;
      }
    >();
    const agentCostTotals = new Map<
      string,
      {
        agentId: string;
        totalCostUsd: number;
        inputTokens: number;
        outputTokens: number;
        invocationCount: number;
      }
    >();
    const dailyMap = new Map<
      string,
      {
        date: string;
        inputTokens: number;
        outputTokens: number;
        cacheReadTokens: number;
        cacheWriteTokens: number;
        totalTokens: number;
        totalCostUsd: number;
      }
    >();

    let totalInvocations = 0;
    let totalInputTokens = 0;
    let totalOutputTokens = 0;
    let totalCacheReadTokens = 0;
    let totalCacheWriteTokens = 0;
    let totalTokens = 0;
    let totalCostUsd = 0;
    let rangeFrom: string | undefined;
    let rangeTo: string | undefined;
    let sessionsWithAgentUsage = 0;
    let sessionsWithTokenUsage = 0;

    for (const session of sessions) {
      const windowUsage = getSessionAgentUsage(selectedWindow, session.id);
      const tokenUsage = getSessionTokenUsage(session.id);
      if (!windowUsage) {
        continue;
      }
      sessionsWithAgentUsage += 1;

      rangeFrom =
        !rangeFrom || new Date(windowUsage.from).getTime() < new Date(rangeFrom).getTime()
          ? windowUsage.from
          : rangeFrom;
      rangeTo =
        !rangeTo || new Date(windowUsage.to).getTime() > new Date(rangeTo).getTime()
          ? windowUsage.to
          : rangeTo;

      for (const agent of windowUsage.agents) {
        totalInvocations += agent.invocationCount;
        const existingAgent = agentUsageMap.get(agent.agentId) ?? {
          agentName: agent.agentName,
          invocationCount: 0,
          skills: new Map<string, { skillName: string; invocationCount: number }>(),
          sessionLogs: []
        };
        existingAgent.invocationCount += agent.invocationCount;
        for (const skill of agent.skills) {
          const existingSkill = existingAgent.skills.get(skill.skillId) ?? {
            skillName: skill.skillName,
            invocationCount: 0
          };
          existingSkill.invocationCount += skill.invocationCount;
          existingAgent.skills.set(skill.skillId, existingSkill);

          const totalSkill = skillTotals.get(skill.skillId) ?? {
            skillName: skill.skillName,
            invocationCount: 0
          };
          totalSkill.invocationCount += skill.invocationCount;
          skillTotals.set(skill.skillId, totalSkill);
        }
        existingAgent.sessionLogs.push({
          sessionId: session.id,
          sessionTitle: session.title,
          ownerId: session.ownerId,
          from: windowUsage.from,
          to: windowUsage.to,
          invocationCount: agent.invocationCount,
          skills: [...agent.skills]
        });
        agentUsageMap.set(agent.agentId, existingAgent);
      }

      if (!tokenUsage) {
        continue;
      }
      sessionsWithTokenUsage += 1;

      const fromDay = windowUsage.from.slice(0, 10);
      const toDay = windowUsage.to.slice(0, 10);
      const inRangeDaily =
        selectedWindow === "all"
          ? tokenUsage.daily
          : tokenUsage.daily.filter((point) => {
              const pointDay = point.date.slice(0, 10);
              return pointDay >= fromDay && pointDay <= toDay;
            });
      const windowTotalTokens =
        selectedWindow === "all"
          ? tokenUsage.totals.totalTokens
          : inRangeDaily.reduce((sum, point) => sum + point.totalTokens, 0);
      const windowTotalCostUsd =
        selectedWindow === "all"
          ? tokenUsage.totals.totalCostUsd
          : inRangeDaily.reduce((sum, point) => sum + point.totalCostUsd, 0);
      const sessionScale =
        selectedWindow === "all"
          ? 1
          : tokenUsage.totals.totalTokens > 0
            ? windowTotalTokens / tokenUsage.totals.totalTokens
            : 0;

      for (const point of inRangeDaily) {
        const existingPoint = dailyMap.get(point.date) ?? {
          date: point.date,
          inputTokens: 0,
          outputTokens: 0,
          cacheReadTokens: 0,
          cacheWriteTokens: 0,
          totalTokens: 0,
          totalCostUsd: 0
        };
        existingPoint.inputTokens += point.inputTokens;
        existingPoint.outputTokens += point.outputTokens;
        existingPoint.cacheReadTokens += point.cacheReadTokens;
        existingPoint.cacheWriteTokens += point.cacheWriteTokens;
        existingPoint.totalTokens += point.totalTokens;
        existingPoint.totalCostUsd += point.totalCostUsd;
        dailyMap.set(point.date, existingPoint);
      }

      totalInputTokens += inRangeDaily.reduce((sum, point) => sum + point.inputTokens, 0);
      totalOutputTokens += inRangeDaily.reduce((sum, point) => sum + point.outputTokens, 0);
      totalCacheReadTokens += inRangeDaily.reduce((sum, point) => sum + point.cacheReadTokens, 0);
      totalCacheWriteTokens += inRangeDaily.reduce((sum, point) => sum + point.cacheWriteTokens, 0);
      totalTokens += windowTotalTokens;
      totalCostUsd += windowTotalCostUsd;

      for (const model of tokenUsage.models) {
        const existingModel = modelTotals.get(model.modelId) ?? {
          modelId: model.modelId,
          inputTokens: 0,
          outputTokens: 0,
          cacheReadTokens: 0,
          cacheWriteTokens: 0,
          totalCostUsd: 0
        };
        existingModel.inputTokens += Math.round(model.inputTokens * sessionScale);
        existingModel.outputTokens += Math.round(model.outputTokens * sessionScale);
        existingModel.cacheReadTokens += Math.round(model.cacheReadTokens * sessionScale);
        existingModel.cacheWriteTokens += Math.round(model.cacheWriteTokens * sessionScale);
        existingModel.totalCostUsd += model.totalCostUsd * sessionScale;
        modelTotals.set(model.modelId, existingModel);
      }

      for (const agentCost of tokenUsage.agents) {
        const existingAgentCost = agentCostTotals.get(agentCost.agentId) ?? {
          agentId: agentCost.agentId,
          totalCostUsd: 0,
          inputTokens: 0,
          outputTokens: 0,
          invocationCount: 0
        };
        existingAgentCost.totalCostUsd += agentCost.totalCostUsd * sessionScale;
        existingAgentCost.inputTokens += Math.round(agentCost.inputTokens * sessionScale);
        existingAgentCost.outputTokens += Math.round(agentCost.outputTokens * sessionScale);
        existingAgentCost.invocationCount += Math.round(agentCost.invocationCount * sessionScale);
        agentCostTotals.set(agentCost.agentId, existingAgentCost);
      }
    }

    const agents = Array.from(agentUsageMap.entries())
      .map(([agentId, data]) => ({
        agentId,
        agentName: data.agentName,
        invocationCount: data.invocationCount,
        skills: Array.from(data.skills.entries())
          .map(([skillId, skill]) => ({ skillId, ...skill }))
          .sort((a, b) => b.invocationCount - a.invocationCount),
        sessionLogs: data.sessionLogs.sort(
          (a, b) => new Date(b.to).getTime() - new Date(a.to).getTime()
        )
      }))
      .sort((a, b) => b.invocationCount - a.invocationCount);

    const skills = Array.from(skillTotals.entries())
      .map(([skillId, data]) => ({ skillId, ...data }))
      .sort((a, b) => b.invocationCount - a.invocationCount);
    const models = Array.from(modelTotals.values()).sort((a, b) => b.totalCostUsd - a.totalCostUsd);
    const agentCosts = Array.from(agentCostTotals.values()).sort(
      (a, b) => b.totalCostUsd - a.totalCostUsd
    );
    const daily = Array.from(dailyMap.values()).sort(
      (a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()
    );

    return {
      rangeFrom,
      rangeTo,
      totalInvocations,
      totalInputTokens,
      totalOutputTokens,
      totalCacheReadTokens,
      totalCacheWriteTokens,
      totalTokens,
      totalCostUsd,
      sessionCount: sessions.length,
      sessionsWithAgentUsage,
      sessionsWithTokenUsage,
      agents,
      skills,
      models,
      agentCosts,
      daily
    };
  }, [sessions, selectedWindow]);

  const [selectedAgentId, setSelectedAgentId] = useState<string | null>(null);
  const selectedAgent =
    aggregated.agents.find((agent) => agent.agentId === selectedAgentId) ?? aggregated.agents[0];

  const tabs: { id: WorkbenchAgentsTab; label: string }[] = [
    { id: "overview", label: "Overview" },
    { id: "models", label: "Models" },
    { id: "daily", label: "Daily" },
    { id: "agents", label: "Agents" }
  ];

  return (
    <div className="f-grid">
      <section className="f-card">
        <div className="f-workbench-agents-head">
          <h3>Workbench Agents</h3>
          <div className="f-workbench-agents-controls">
            <label className="f-meta-line" htmlFor="workbench-agent-window">
              Window
            </label>
            <select
              id="workbench-agent-window"
              className="f-session-select"
              value={selectedWindow}
              onChange={(event) => setSelectedWindow(event.target.value)}
            >
              {windows.map((window) => (
                <option key={window.id} value={window.id}>
                  {window.label}
                </option>
              ))}
            </select>
          </div>
        </div>
        <p className="f-meta-line">
          Range:{" "}
          <span className="f-tech">
            {aggregated.rangeFrom && aggregated.rangeTo
              ? `${formatDateTime(aggregated.rangeFrom)} - ${formatDateTime(aggregated.rangeTo)}`
              : "No data"}
          </span>
        </p>
        <p className="f-meta-line">
          Coverage:{" "}
          <span className="f-tech">
            {aggregated.sessionsWithAgentUsage}/{aggregated.sessionCount}
          </span>{" "}
          sessions with agent usage,{" "}
          <span className="f-tech">
            {aggregated.sessionsWithTokenUsage}/{aggregated.sessionCount}
          </span>{" "}
          sessions with token usage.
        </p>
        <div className="f-workbench-agents-kpi-grid">
          <section className="f-card f-card--nested">
            <h4 className="f-subtitle">Total tokens</h4>
            <p className="f-tech f-workbench-agents-kpi-value">
              {formatTokenCount(aggregated.totalTokens)}
            </p>
            <p className="f-meta-line">
              In/Out:{" "}
              <span className="f-tech">
                {formatTokenCount(aggregated.totalInputTokens)} /{" "}
                {formatTokenCount(aggregated.totalOutputTokens)}
              </span>
            </p>
            <p className="f-meta-line">
              CR/CW:{" "}
              <span className="f-tech">
                {formatTokenCount(aggregated.totalCacheReadTokens)} /{" "}
                {formatTokenCount(aggregated.totalCacheWriteTokens)}
              </span>
            </p>
          </section>
          <section className="f-card f-card--nested">
            <h4 className="f-subtitle">Total cost</h4>
            <p className="f-tech f-workbench-agents-kpi-value">
              {formatCurrencyUsd(aggregated.totalCostUsd)}
            </p>
            <p className="f-meta-line">
              Models: <span className="f-tech">{aggregated.models.length}</span>
            </p>
            <p className="f-meta-line">
              Agents: <span className="f-tech">{aggregated.agents.length}</span>
            </p>
          </section>
          <section className="f-card f-card--nested">
            <h4 className="f-subtitle">Invocations</h4>
            <p className="f-tech f-workbench-agents-kpi-value">{aggregated.totalInvocations}</p>
            <p className="f-meta-line">
              Skills tracked: <span className="f-tech">{aggregated.skills.length}</span>
            </p>
          </section>
        </div>

        <div className="f-workbench-agents-tabs">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              type="button"
              className={`f-workbench-agents-tab${
                activeTab === tab.id ? " f-workbench-agents-tab--active" : ""
              }`}
              onClick={() => setActiveTab(tab.id)}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {activeTab === "overview" ? (
          <div className="f-grid">
            <section className="f-card f-card--nested">
              <h4 className="f-subtitle">Tokens per day</h4>
              <TokenUsageTimeline daily={aggregated.daily} />
            </section>
            <div className="f-grid f-grid--2">
              <TokenCostBars
                title="Models by cost"
                items={aggregated.models.map((model) => ({
                  id: model.modelId,
                  label: `${model.modelId} (${formatPercent(
                    (model.totalCostUsd / Math.max(aggregated.totalCostUsd, 0.001)) * 100
                  )})`,
                  totalCostUsd: model.totalCostUsd,
                  detail: `In: ${formatTokenCount(model.inputTokens)} • Out: ${formatTokenCount(
                    model.outputTokens
                  )}`,
                  secondaryDetail: `CR: ${formatTokenCount(
                    model.cacheReadTokens
                  )} • CW: ${formatTokenCount(model.cacheWriteTokens)}`
                }))}
              />
              <TokenCostBars
                title="Agents by cost"
                items={aggregated.agentCosts.map((agent) => ({
                  id: agent.agentId,
                  label: `${agent.agentId} (${formatPercent(
                    (agent.totalCostUsd / Math.max(aggregated.totalCostUsd, 0.001)) * 100
                  )})`,
                  totalCostUsd: agent.totalCostUsd,
                  detail: `Tokens: ${formatTokenCount(agent.inputTokens + agent.outputTokens)}`,
                  secondaryDetail: `Invocations: ${agent.invocationCount}`
                }))}
              />
            </div>
          </div>
        ) : null}

        {activeTab === "models" ? (
          <section className="f-card f-card--nested">
            <h4 className="f-subtitle">Models by cost</h4>
            <ul className="f-list f-list--plain f-workbench-model-list">
              {aggregated.models.map((model) => (
                <li key={model.modelId} className="f-workbench-model-item">
                  <div className="f-workbench-model-head">
                    <p className="f-tech">{model.modelId}</p>
                    <p className="f-tech">{formatCurrencyUsd(model.totalCostUsd)}</p>
                  </div>
                  <p className="f-meta-line">
                    Share:{" "}
                    <span className="f-tech">
                      {formatPercent(
                        (model.totalCostUsd / Math.max(aggregated.totalCostUsd, 0.001)) * 100
                      )}
                    </span>
                  </p>
                  <p className="f-meta-line">
                    In: <span className="f-tech">{formatTokenCount(model.inputTokens)}</span> • Out:{" "}
                    <span className="f-tech">{formatTokenCount(model.outputTokens)}</span> • CR:{" "}
                    <span className="f-tech">{formatTokenCount(model.cacheReadTokens)}</span> • CW:{" "}
                    <span className="f-tech">{formatTokenCount(model.cacheWriteTokens)}</span>
                  </p>
                </li>
              ))}
              {aggregated.models.length === 0 ? <li>No model data for selected window.</li> : null}
            </ul>
          </section>
        ) : null}

        {activeTab === "daily" ? (
          <section className="f-card f-card--nested">
            <h4 className="f-subtitle">Daily token and cost log</h4>
            <TokenUsageTimeline daily={aggregated.daily} />
            <ul className="f-list f-list--plain f-token-daily-log">
              {aggregated.daily
                .slice()
                .reverse()
                .map((point) => (
                  <li key={`${point.date}-workbench`} className="f-token-daily-log-item">
                    <span className="f-tech">
                      {new Date(point.date).toLocaleDateString("en-IN", {
                        month: "short",
                        day: "2-digit"
                      })}
                    </span>
                    <span className="f-tech">
                      {formatTokenCount(point.totalTokens)} tokens
                    </span>
                    <span className="f-tech">{formatCurrencyUsd(point.totalCostUsd)}</span>
                  </li>
                ))}
              {aggregated.daily.length === 0 ? (
                <li className="f-meta-line">No daily data for selected window.</li>
              ) : null}
            </ul>
          </section>
        ) : null}

        {activeTab === "agents" ? (
          <div className="f-grid">
            <div className="f-agent-card-grid">
              {aggregated.agents.map((agent) => (
                <button
                  key={agent.agentId}
                  type="button"
                  className={`f-agent-card${
                    selectedAgent?.agentId === agent.agentId ? " f-agent-card--active" : ""
                  }`}
                  onClick={() => setSelectedAgentId(agent.agentId)}
                >
                  <p className="f-agent-card-title f-tech">{agent.agentName}</p>
                  <p className="f-agent-card-meta">
                    <span className="f-tech">{agent.invocationCount}</span> invocations
                  </p>
                  <p className="f-agent-card-meta">
                    <span className="f-tech">{agent.skills.length}</span> skills
                  </p>
                  <p className="f-agent-card-meta">
                    Top:{" "}
                    <span className="f-tech">
                      {agent.skills
                        .slice(0, 2)
                        .map((skill) => `${skill.skillName} (${skill.invocationCount})`)
                        .join(", ")}
                    </span>
                  </p>
                </button>
              ))}
            </div>
            {selectedAgent ? (
              <section className="f-card f-card--nested">
                <h4 className="f-subtitle">
                  Agent usage log — <span className="f-tech">{selectedAgent.agentName}</span>
                </h4>
                <div className="f-agent-log-terminal">
                  {selectedAgent.sessionLogs.map((log) => (
                    <div key={`${selectedAgent.agentId}-${log.sessionId}`} className="f-agent-log-block">
                      <p className="f-agent-log-line">
                        <span className="f-tech f-agent-log-ts">
                          {formatLogTimestamp(log.from)}
                        </span>{" "}
                        <span className="f-agent-log-level">INFO</span>{" "}
                        <span className="f-tech">session.start</span>{" "}
                        <Link
                          to={workspaceSessionPath(workbenchId, log.sessionId)}
                          className="f-text-link"
                        >
                          <span className="f-session-inline-icon" aria-hidden="true">
                            {SESSION_ICON}
                          </span>{" "}
                          <span className="f-tech">{log.sessionId}</span>
                        </Link>{" "}
                        owner=<span className="f-tech">{resolvePersonName(log.ownerId)}</span>
                      </p>
                      <p className="f-agent-log-line">
                        <span className="f-tech f-agent-log-ts">
                          {formatLogTimestamp(log.to)}
                        </span>{" "}
                        <span className="f-agent-log-level">INFO</span>{" "}
                        <span className="f-tech">agent.summary</span>{" "}
                        invocations=<span className="f-tech">{log.invocationCount}</span> session=
                        <span className="f-tech">{log.sessionTitle}</span>
                      </p>
                      {log.skills.map((skill) => (
                        <p key={skill.skillId} className="f-agent-log-line">
                          <span className="f-tech f-agent-log-ts">
                            {formatLogTimestamp(log.to)}
                          </span>{" "}
                          <span className="f-agent-log-level">INFO</span>{" "}
                          <span className="f-tech">skill.invocation</span>{" "}
                          skill=<span className="f-tech">{skill.skillName}</span> count=
                          <span className="f-tech">{skill.invocationCount}</span>
                        </p>
                      ))}
                    </div>
                  ))}
                </div>
              </section>
            ) : (
              <p className="f-meta-line">No agent data for selected window.</p>
            )}
          </div>
        ) : null}
      </section>
    </div>
  );
}

function toneForRiskLevel(riskLevel: string) {
  if (riskLevel === "high") return "governance-hard-block" as const;
  if (riskLevel === "medium") return "warning" as const;
  return "success" as const;
}

function toneForWorkOrderStatus(status: string) {
  if (status === "blocked") return "blocked" as const;
  if (status === "in-progress") return "info" as const;
  if (status === "queued") return "warning" as const;
  return "success" as const;
}

export function ConsoleContent() {
  const { workbenchId, consoleId } = useParams<{
    workbenchId: string;
    consoleId: string;
  }>();
  const [showArchivedWorkspacesByType, setShowArchivedWorkspacesByType] = useState<
    Record<(typeof WORKSPACE_TYPE_ORDER)[number], boolean>
  >(() =>
    WORKSPACE_TYPE_ORDER.reduce(
      (acc, workspaceType) => {
        acc[workspaceType] = false;
        return acc;
      },
      {} as Record<(typeof WORKSPACE_TYPE_ORDER)[number], boolean>
    )
  );
  const [infraClusterFilter, setInfraClusterFilter] = useState("all");
  const [infraHealthFilter, setInfraHealthFilter] = useState("all");
  const [infraSortBy, setInfraSortBy] = useState<"health" | "cpu" | "heartbeat">("health");

  if (!workbenchId || !consoleId) {
    return null;
  }
  const consoleDef = getConsoleById(consoleId);
  if (!consoleDef) {
    return (
      <ConsolePage
        title="Unknown Console"
        primaryQuestion="Console not found."
        pattern="landing"
        state="error"
      >
        <p>Console ID <span className="f-tech">{consoleId}</span> is not registered.</p>
      </ConsolePage>
    );
  }

  const isScenarioWorkbench = workbenchId === scenario.defaultWorkbenchId;
  const intents = getIntentsForWorkbench(workbenchId);
  const workOrders = getWorkOrdersForWorkbench(workbenchId);
  const team = getWorkbenchTeam(workbenchId);

  const body = renderConsoleBody(consoleId, {
    workbenchId,
    isScenarioWorkbench,
    intents,
    workOrders,
    team,
    showArchivedWorkspacesByType,
    setShowArchivedWorkspacesByType,
    infraClusterFilter,
    setInfraClusterFilter,
    infraHealthFilter,
    setInfraHealthFilter,
    infraSortBy,
    setInfraSortBy
  });

  return (
    <ConsolePage
      title={consoleDef.label}
      primaryQuestion={consoleDef.primaryQuestion}
      pattern={consoleDef.pattern}
    >
      {body}
    </ConsolePage>
  );
}

type RenderContext = {
  workbenchId: string;
  isScenarioWorkbench: boolean;
  intents: ReturnType<typeof getIntentsForWorkbench>;
  workOrders: ReturnType<typeof getWorkOrdersForWorkbench>;
  team: ReturnType<typeof getWorkbenchTeam>;
  showArchivedWorkspacesByType: Record<(typeof WORKSPACE_TYPE_ORDER)[number], boolean>;
  setShowArchivedWorkspacesByType: (
    value: Record<(typeof WORKSPACE_TYPE_ORDER)[number], boolean>
  ) => void;
  infraClusterFilter: string;
  setInfraClusterFilter: (value: string) => void;
  infraHealthFilter: string;
  setInfraHealthFilter: (value: string) => void;
  infraSortBy: "health" | "cpu" | "heartbeat";
  setInfraSortBy: (value: "health" | "cpu" | "heartbeat") => void;
};

function renderConsoleBody(consoleId: string, ctx: RenderContext) {
  const {
    workbenchId,
    isScenarioWorkbench,
    intents,
    workOrders,
    team,
    showArchivedWorkspacesByType,
    setShowArchivedWorkspacesByType,
    infraClusterFilter,
    setInfraClusterFilter,
    infraHealthFilter,
    setInfraHealthFilter,
    infraSortBy,
    setInfraSortBy
  } = ctx;

  switch (consoleId) {
    case "work-overview":
      return (
        <div className="f-grid">
          <div className="f-card">
            <h3>Attention Queue</h3>
            <ul className="f-list">
              {workOrders
                .filter((wo) => wo.status === "blocked" || wo.status === "in-progress")
                .map((wo) => (
                  <li key={wo.id}>
                    <span className="f-tech">{wo.id}</span> {wo.title}
                    <StatusBadge tone={wo.status === "blocked" ? "blocked" : "info"}>
                      {wo.status}
                    </StatusBadge>
                  </li>
                ))}
            </ul>
          </div>
        </div>
      );

    case "orchestration":
      return (
        <div className="f-grid">
          <div className="f-card">
            <h3>Product Intents</h3>
            <ul className="f-list">
              {intents.map((pi) => (
                <li key={pi.id}>
                  <Link
                    to={orchestrationItemPath(workbenchId, "product-intent", pi.id)}
                    className="f-text-link"
                  >
                    <span className="f-tech">{pi.id}</span> {pi.title}
                  </Link>
                  <StatusBadge tone="info">{pi.stage}</StatusBadge>
                </li>
              ))}
            </ul>
          </div>
          <div className="f-card">
            <h3>Discovery Cases</h3>
            <ul className="f-list">
              {discoveryCases
                .filter((dc) => dc.workbenchId === workbenchId)
                .map((dc) => (
                  <li key={dc.id}>
                    <Link
                      to={orchestrationItemPath(workbenchId, "discovery-case", dc.id)}
                      className="f-text-link"
                    >
                      <span className="f-tech">{dc.id}</span> {dc.title}
                    </Link>
                  </li>
                ))}
            </ul>
          </div>
          <div className="f-card">
            <h3>Release Intents</h3>
            <ul className="f-list">
              {getReleaseIntentsForWorkbench(workbenchId).map((releaseIntent) => (
                <li key={releaseIntent.id}>
                  <Link
                    to={orchestrationItemPath(workbenchId, "release-intent", releaseIntent.id)}
                    className="f-text-link"
                  >
                    <span className="f-tech">{releaseIntent.id}</span>{" "}
                    {releaseIntent.title}
                  </Link>
                  <div className="f-inline-row">
                    <StatusBadge tone={toneForRiskLevel(releaseIntent.riskLevel)}>
                      {`${releaseIntent.riskLevel} risk`}
                    </StatusBadge>
                    <StatusBadge tone="info">{releaseIntent.stage}</StatusBadge>
                  </div>
                  <p className="f-meta-line">
                    Target window: <span className="f-tech">{formatDateTime(releaseIntent.targetReleaseWindow)}</span>
                  </p>
                </li>
              ))}
            </ul>
          </div>
        </div>
      );

    case "progress":
      return (
        <div className="f-card">
          <h3>Progress by Track</h3>
          <p>
            Completed WOs: {workOrders.filter((wo) => wo.status === "completed").length} /{" "}
            {workOrders.length}
          </p>
        </div>
      );

    case "work-rituals":
      return <GenericPlaceholder label="Work rituals and sprint cadence" />;

    case "my-work":
      return (
        <div className="f-card">
          <h3>My Day</h3>
          <ul className="f-list">
            {workOrders.slice(0, 3).map((wo) => (
              <li key={wo.id}>
                <span className="f-tech">{wo.id}</span> {wo.title}
              </li>
            ))}
          </ul>
        </div>
      );

    case "workspaces-overview":
      {
        const allSessions = getWorkspaceSessionsForWorkbench(workbenchId);
        return (
          <div className="f-workspaces-type-grid">
            {WORKSPACE_TYPE_ORDER.map((workspaceType) => {
              const showArchivedForType =
                showArchivedWorkspacesByType[workspaceType];
              const sessionsForType = allSessions.filter((session) => {
                if (session.workspaceType !== workspaceType) {
                  return false;
                }
                if (showArchivedForType) {
                  return true;
                }
                return session.status === "active";
              });
              return (
                <section key={workspaceType} className="f-card f-card--nested">
                  <div className="f-workspaces-card-header">
                    <h4 className="f-subtitle f-workspace-type-title">
                      <span className="f-workspace-type-icon" aria-hidden="true">
                        {workspaceTypeIcon(workspaceType)}
                      </span>
                      <span>{workspaceTypeLabel(workspaceType)}</span>
                    </h4>
                    <details className="f-workspaces-overview-menu">
                      <summary
                        className="f-workspaces-overview-menu-trigger"
                        aria-label={`${workspaceTypeLabel(workspaceType)} options`}
                      >
                        <span className="f-tech">⋮</span>
                      </summary>
                      <div className="f-workspaces-overview-menu-content">
                        <label className="f-workspaces-overview-menu-option">
                          <input
                            type="checkbox"
                            checked={showArchivedForType}
                            onChange={(event) =>
                              setShowArchivedWorkspacesByType({
                                ...showArchivedWorkspacesByType,
                                [workspaceType]: event.target.checked
                              })
                            }
                          />
                          <span>Show archived workspaces</span>
                        </label>
                      </div>
                    </details>
                  </div>
                  <ul className="f-list f-list--plain f-workspace-session-list">
                    {sessionsForType.map((session) => (
                      <li key={session.id} className="f-workspace-session-item">
                        {(() => {
                          const openWorkOrders = session.workOrderIds
                            .map((workOrderId) => getWorkOrder(workOrderId))
                            .filter(
                              (workOrder): workOrder is NonNullable<typeof workOrder> =>
                                Boolean(workOrder)
                            )
                            .filter((workOrder) => workOrder.status !== "completed");
                          return (
                        <Link
                          to={workspaceSessionPath(workbenchId, session.id)}
                          className="f-workspace-session-card"
                        >
                          <div className="f-workspace-session-head">
                            <span className="f-workspace-session-icon" aria-hidden="true">
                              🖥
                            </span>
                            <div>
                              <p className="f-workspace-session-title">{session.title}</p>
                              <p className="f-workspace-session-id f-tech">{session.id}</p>
                            </div>
                          </div>
                          <div className="f-workspace-session-meta">
                            {(() => {
                              const ownerName = resolvePersonName(session.ownerId);
                              const ownerProfile = getTeamMemberProfile(session.ownerId);
                              return (
                                <>
                                  <span className="f-workspace-owner">
                                    {ownerProfile?.avatarUrl ? (
                                      <img
                                        src={ownerProfile.avatarUrl}
                                        alt={ownerName}
                                        className="f-workspace-owner-avatar"
                                      />
                                    ) : (
                                      <span className="f-workspace-owner-avatar f-workspace-owner-avatar--initials">
                                        {initialsForName(ownerName)}
                                      </span>
                                    )}
                                    <span className="f-workspace-owner-name">{ownerName}</span>
                                  </span>
                                  <span className="f-workspace-session-pill f-tech">
                                    {session.status}
                                  </span>
                                  <span className="f-workspace-session-pill">
                                    ⏱{" "}
                                    <span className="f-tech">
                                      {formatDuration(
                                        Math.max(
                                          1,
                                          Math.round(
                                            (new Date(session.lastUpdatedAt).getTime() -
                                              new Date(session.startedAt).getTime()) /
                                              (60 * 1000)
                                          )
                                        )
                                      )}
                                    </span>
                                  </span>
                                </>
                              );
                            })()}
                          </div>
                          <div className="f-workspace-session-open-wos">
                            <p className="f-workspace-session-open-wos-title">Open work orders</p>
                            <ul className="f-list f-list--plain f-workspace-session-open-wos-list">
                              {openWorkOrders.slice(0, 3).map((workOrder) => (
                                <li key={workOrder.id}>
                                  <span className="f-tech">{workOrder.id}</span> {workOrder.title}
                                </li>
                              ))}
                              {openWorkOrders.length > 3 ? (
                                <li className="f-meta-line">
                                  +{openWorkOrders.length - 3} more open work orders
                                </li>
                              ) : null}
                              {openWorkOrders.length === 0 ? (
                                <li className="f-meta-line">No open work orders in this session.</li>
                              ) : null}
                            </ul>
                          </div>
                        </Link>
                          );
                        })()}
                      </li>
                    ))}
                    {sessionsForType.length === 0 ? (
                      <li>No workspaces in this state.</li>
                    ) : null}
                  </ul>
                </section>
              );
            })}
          </div>
        );
      }

    case "workspace-infrastructure":
      {
        const sessions = getWorkspaceSessionsForWorkbench(workbenchId);
        const runningPods = sessions
          .map((session) => {
            const pod = getSessionCoderPod(session.id)?.activePod;
            if (!pod || pod.status !== "running") {
              return undefined;
            }
            return {
              sessionId: session.id,
              sessionTitle: session.title,
              ownerId: session.ownerId,
              workspaceType: session.workspaceType,
              podId: pod.id,
              status: pod.status,
              cluster: pod.cluster,
              namespace: pod.namespace,
              cpuCores: pod.resources.cpuCores,
              memoryGiB: pod.resources.memoryGiB,
              storageGiB: pod.resources.ephemeralStorageGiB,
              heartbeatAt: pod.lastHeartbeatAt,
              startedAt: pod.startedAt,
              healthStatus: pod.health.status,
              healthScore: pod.health.score,
              healthIssues: pod.health.issues
            };
          })
          .filter((pod): pod is NonNullable<typeof pod> => Boolean(pod));

        const referenceNowMs = Math.max(
          ...runningPods.map((pod) => new Date(pod.heartbeatAt).getTime()),
          Date.now()
        );

        const healthRank = (status: string) => {
          if (status === "healthy") return 2;
          if (status === "degraded") return 1;
          return 0;
        };

        const filteredPods = runningPods.filter((pod) => {
          if (infraClusterFilter !== "all" && pod.cluster !== infraClusterFilter) {
            return false;
          }
          if (infraHealthFilter !== "all" && pod.healthStatus !== infraHealthFilter) {
            return false;
          }
          return true;
        });

        const sortedPods = [...filteredPods].sort((a, b) => {
          if (infraSortBy === "cpu") {
            return b.cpuCores - a.cpuCores;
          }
          if (infraSortBy === "heartbeat") {
            return new Date(a.heartbeatAt).getTime() - new Date(b.heartbeatAt).getTime();
          }
          return healthRank(a.healthStatus) - healthRank(b.healthStatus);
        });

        const podsByCluster = new Map<
          string,
          {
            pods: typeof filteredPods;
            totals: {
              cpuCores: number;
              memoryGiB: number;
              storageGiB: number;
              healthyCount: number;
              degradedCount: number;
              unhealthyCount: number;
            };
          }
        >();
        for (const pod of filteredPods) {
          const existing = podsByCluster.get(pod.cluster) ?? {
            pods: [],
            totals: {
              cpuCores: 0,
              memoryGiB: 0,
              storageGiB: 0,
              healthyCount: 0,
              degradedCount: 0,
              unhealthyCount: 0
            }
          };
          existing.pods.push(pod);
          existing.totals.cpuCores += pod.cpuCores;
          existing.totals.memoryGiB += pod.memoryGiB;
          existing.totals.storageGiB += pod.storageGiB;
          if (pod.healthStatus === "healthy") existing.totals.healthyCount += 1;
          else if (pod.healthStatus === "degraded") existing.totals.degradedCount += 1;
          else existing.totals.unhealthyCount += 1;
          podsByCluster.set(pod.cluster, existing);
        }

        const clusterNames = Array.from(new Set(runningPods.map((pod) => pod.cluster))).sort();
        const infraTotals = filteredPods.reduce(
          (acc, pod) => {
            acc.cpuCores += pod.cpuCores;
            acc.memoryGiB += pod.memoryGiB;
            acc.storageGiB += pod.storageGiB;
            if (pod.healthStatus === "healthy") acc.healthy += 1;
            else if (pod.healthStatus === "degraded") acc.degraded += 1;
            else acc.unhealthy += 1;
            return acc;
          },
          { cpuCores: 0, memoryGiB: 0, storageGiB: 0, healthy: 0, degraded: 0, unhealthy: 0 }
        );

        const hasActiveFilters = infraClusterFilter !== "all" || infraHealthFilter !== "all";
        const mostLoadedCluster = Array.from(podsByCluster.entries()).sort(
          (a, b) => b[1].totals.cpuCores - a[1].totals.cpuCores
        )[0];

        const podsWithIssues = sortedPods.filter((pod) => pod.healthIssues.length > 0);
        const stalePods = sortedPods.filter(
          (pod) => referenceNowMs - new Date(pod.heartbeatAt).getTime() > 20 * 60 * 1000
        );

        return (
          <div className="f-grid">
            <section className="f-card">
              <h3>Infrastructure Overview</h3>
              <div className="f-infra-kpi-grid">
                <section className="f-card f-card--nested f-infra-kpi">
                  <h4 className="f-subtitle">Running pods</h4>
                  <p className="f-tech f-infra-kpi-value">{filteredPods.length}</p>
                </section>
                <section className="f-card f-card--nested f-infra-kpi">
                  <h4 className="f-subtitle">Degraded / unhealthy</h4>
                  <p className="f-tech f-infra-kpi-value">
                    {infraTotals.degraded} / {infraTotals.unhealthy}
                  </p>
                </section>
                <section className="f-card f-card--nested f-infra-kpi">
                  <h4 className="f-subtitle">Total resources</h4>
                  <p className="f-tech f-infra-kpi-value">
                    {infraTotals.cpuCores} CPU • {infraTotals.memoryGiB} GiB •{" "}
                    {infraTotals.storageGiB} GiB
                  </p>
                </section>
                <section className="f-card f-card--nested f-infra-kpi">
                  <h4 className="f-subtitle">Most loaded cluster</h4>
                  <p className="f-tech f-infra-kpi-value">
                    {mostLoadedCluster
                      ? `${mostLoadedCluster[0]} (${mostLoadedCluster[1].totals.cpuCores} CPU)`
                      : filteredPods.length > 0
                        ? "n/a"
                        : "none in current filter"}
                  </p>
                </section>
              </div>
              {hasActiveFilters ? (
                <p className="f-meta-line">
                  Filtered view: <span className="f-tech">{filteredPods.length}</span> of{" "}
                  <span className="f-tech">{runningPods.length}</span> running pods.
                </p>
              ) : null}
              <div className="f-grid f-grid--2">
                <section className="f-card f-card--nested">
                  <h4 className="f-subtitle">Cluster Summary</h4>
                  <ul className="f-list f-list--plain">
                    {Array.from(podsByCluster.entries()).map(([cluster, bucket]) => (
                      <li key={cluster} className="f-infra-cluster-row">
                        <p className="f-tech">{cluster}</p>
                        <p className="f-meta-line">
                          Pods: {bucket.pods.length} • CPU: {bucket.totals.cpuCores} • Memory:{" "}
                          {bucket.totals.memoryGiB} GiB • Storage: {bucket.totals.storageGiB} GiB
                        </p>
                        <p className="f-meta-line">
                          Health: {bucket.totals.healthyCount} healthy, {bucket.totals.degradedCount}{" "}
                          degraded, {bucket.totals.unhealthyCount} unhealthy
                        </p>
                      </li>
                    ))}
                  </ul>
                </section>
                <section className="f-card f-card--nested">
                  <h4 className="f-subtitle">Attention Queue</h4>
                  <p className="f-meta-line">
                    Pods with issues: <span className="f-tech">{podsWithIssues.length}</span>
                  </p>
                  <ul className="f-list">
                    {podsWithIssues.slice(0, 6).map((pod) => (
                      <li key={`${pod.podId}-issue`}>
                        <span className="f-tech">{pod.podId}</span>: {pod.healthIssues.join(", ")}
                      </li>
                    ))}
                    {podsWithIssues.length === 0 ? <li>No current pod health issues.</li> : null}
                  </ul>
                  <p className="f-meta-line">
                    Stale heartbeat pods (&gt;20m):{" "}
                    <span className="f-tech">{stalePods.length}</span>
                  </p>
                </section>
              </div>
              <div className="f-infra-controls">
                <div className="f-infra-control-group">
                  <label className="f-meta-line" htmlFor="infra-cluster-filter">
                    Cluster
                  </label>
                  <select
                    id="infra-cluster-filter"
                    className="f-session-select"
                    value={infraClusterFilter}
                    onChange={(event) => setInfraClusterFilter(event.target.value)}
                  >
                    <option value="all">All clusters</option>
                    {clusterNames.map((cluster) => (
                      <option key={cluster} value={cluster}>
                        {cluster}
                      </option>
                    ))}
                  </select>
                </div>
                <div className="f-infra-control-group">
                  <label className="f-meta-line" htmlFor="infra-health-filter">
                    Health
                  </label>
                  <select
                    id="infra-health-filter"
                    className="f-session-select"
                    value={infraHealthFilter}
                    onChange={(event) => setInfraHealthFilter(event.target.value)}
                  >
                    <option value="all">All health states</option>
                    <option value="healthy">healthy</option>
                    <option value="degraded">degraded</option>
                    <option value="unhealthy">unhealthy</option>
                  </select>
                </div>
                <div className="f-infra-control-group">
                  <label className="f-meta-line" htmlFor="infra-sort">
                    Sort by
                  </label>
                  <select
                    id="infra-sort"
                    className="f-session-select"
                    value={infraSortBy}
                    onChange={(event) =>
                      setInfraSortBy(event.target.value as "health" | "cpu" | "heartbeat")
                    }
                  >
                    <option value="health">Health severity</option>
                    <option value="cpu">CPU usage</option>
                    <option value="heartbeat">Heartbeat recency</option>
                  </select>
                </div>
                <div className="f-inline-row f-infra-control-actions">
                  <button
                    type="button"
                    className="f-button f-button--ghost"
                    onClick={() => {
                      setInfraClusterFilter("all");
                      setInfraHealthFilter("all");
                      setInfraSortBy("health");
                    }}
                    disabled={!hasActiveFilters && infraSortBy === "health"}
                  >
                    Reset filters
                  </button>
                </div>
              </div>
              <div className="f-infra-table-wrap">
                <table className="f-infra-table">
                  <thead>
                    <tr>
                      <th>Pod</th>
                      <th>Cluster</th>
                      <th>Namespace</th>
                      <th>Status</th>
                      <th>Health</th>
                      <th>Resources</th>
                      <th>Session</th>
                      <th>Owner</th>
                      <th>Heartbeat</th>
                    </tr>
                  </thead>
                  <tbody>
                    {sortedPods.map((pod) => (
                      <tr key={pod.podId}>
                        <td className="f-tech">{pod.podId}</td>
                        <td className="f-tech">{pod.cluster}</td>
                        <td className="f-tech">{pod.namespace}</td>
                        <td className="f-tech">{pod.status}</td>
                        <td className="f-tech">
                          {pod.healthStatus} ({pod.healthScore})
                        </td>
                        <td className="f-tech">
                          {pod.cpuCores} CPU / {pod.memoryGiB} GiB / {pod.storageGiB} GiB
                        </td>
                        <td>
                          <Link
                            to={workspaceSessionPath(workbenchId, pod.sessionId)}
                            className="f-text-link"
                          >
                            <span className="f-session-inline-icon" aria-hidden="true">
                              {SESSION_ICON}
                            </span>{" "}
                            <span className="f-tech">{pod.sessionId}</span>
                          </Link>
                          <p className="f-meta-line">{pod.workspaceType}</p>
                        </td>
                        <td className="f-tech">{resolvePersonName(pod.ownerId)}</td>
                        <td className="f-tech">{formatDateTime(pod.heartbeatAt)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div className="f-grid f-grid--2">
                {sortedPods.length === 0 ? (
                  <p className="f-meta-line">No running pods match selected filters.</p>
                ) : null}
              </div>
            </section>
          </div>
        );
      }

    case "workspace-agents":
      return <WorkbenchAgentsConsole workbenchId={workbenchId} />;

    case "ci":
      return isScenarioWorkbench ? (
        <div className="f-card">
          <h3>Pipeline Status</h3>
          <StatusBadge tone="success">Build passing</StatusBadge>
          <p className="f-meta-line">
            Branch <span className="f-tech">wo/WO-3015</span> — blocked at governance gate
          </p>
        </div>
      ) : (
        <GenericPlaceholder label="CI pipeline status" />
      );

    case "components":
      return <GenericPlaceholder label="Systems and component ontology" />;

    case "findings":
      return (
        <div className="f-card">
          <h3>Open Findings</h3>
          <StatusBadge tone="warning">2 medium severity</StatusBadge>
        </div>
      );

    case "quality-status":
      return isScenarioWorkbench ? (
        <div className="f-grid">
          <div className="f-card">
            <h3>Test Results (Build metrics)</h3>
            <p>Coverage: 78% — trend stable</p>
            <StatusBadge tone="info">Build-time quality</StatusBadge>
          </div>
          <BuildTrackPanel />
        </div>
      ) : (
        <GenericPlaceholder label="Test results and coverage trends" />
      );

    case "release-artifacts":
      return isScenarioWorkbench ? <BuildTrackPanel /> : (
        <GenericPlaceholder label="Release artifacts and deployment status" />
      );

    case "workforce-overview":
      return team ? (
        <div className="f-card">
          <h3>Capacity Summary</h3>
          <p>
            {team.productManagers.length} PMs, {team.developers.length} developers,{" "}
            {team.qaPeople.length} QA
          </p>
        </div>
      ) : (
        <GenericPlaceholder label="Workforce overview" />
      );

    case "team":
      return team ? (
        <div className="f-card">
          <h3>Team Roster</h3>
          <ul className="f-list">
            {[...team.productManagers, ...team.developers, ...team.qaPeople].map(
              (person) => (
                <li key={person.id}>
                  <Link to={teamMemberPath(workbenchId, person.id)} className="f-text-link">
                    {person.name}
                  </Link>
                  <span className="f-tech"> ({person.role})</span>
                </li>
              )
            )}
          </ul>
        </div>
      ) : (
        <GenericPlaceholder label="Team roster" />
      );

    case "agent":
      return (
        <div className="f-card">
          <h3>Employed Agents</h3>
          <ul className="f-list">
            <li>agent-spec-drafter</li>
            <li>agent-upi-conformance</li>
            <li>agent-test-planner</li>
          </ul>
        </div>
      );

    case "governance":
      return (
        <div className="f-grid">
          <div className="f-card">
            <h3>Governance Health</h3>
            {isScenarioWorkbench ? (
              <ul className="f-list">
                {getGovernanceForIntent(scenario.selectedProductIntentId).map((gv) => (
                  <li key={gv.id}>
                    <span className="f-tech">{gv.gate}</span>: {gv.summary}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No active governance items for this workbench focus.</p>
            )}
          </div>
        </div>
      );

    case "rituals":
      return <GenericPlaceholder label="Governance ritual calendar" />;

    case "controls":
      return isScenarioWorkbench ? (
        <div className="f-card">
          <h3>Enforcement Queue</h3>
          <StatusBadge tone="governance-hard-block">Hard block active</StatusBadge>
          <p className="f-meta-line">Release package review — settlement controls incomplete</p>
        </div>
      ) : (
        <GenericPlaceholder label="Controls and enforcement" />
      );

    case "registers":
      return <GenericPlaceholder label="Risk, debt, and exception registers" />;

    case "reports":
      return <GenericPlaceholder label="Governance reports and dashboards" />;

    case "quality-compliance":
      return isScenarioWorkbench ? (
        <div className="f-card">
          <h3>Quality Threshold Evaluation</h3>
          {governanceVerdicts
            .filter((gv) => gv.orchestrationItemId === scenario.selectedProductIntentId)
            .map((gv) => (
              <div key={gv.id} className="f-meta-line">
                <span className="f-tech">{gv.gate}</span>: {gv.verdict} ({gv.blockType})
                <p>{gv.summary}</p>
              </div>
            ))}
        </div>
      ) : (
        <GenericPlaceholder label="Quality controls threshold evaluation" />
      );

    case "repositories":
      return (
        <div className="f-card">
          <h3>Repositories</h3>
          <p className="f-tech">payment-gateway-core</p>
          <p className="f-tech">payment-gateway-settlement</p>
        </div>
      );

    case "admin":
    case "governance-admin":
      return <GenericPlaceholder label="Workbench configuration" />;

    default:
      return <GenericPlaceholder label="Console content" />;
  }
}

export function OrchestrationItemDetail() {
  const { workbenchId, type, itemId } = useParams<{
    workbenchId: string;
    type: string;
    itemId: string;
  }>();

  if (!workbenchId || !type || !itemId) {
    return null;
  }

  const workbench = getWorkbench(workbenchId);
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const isScenarioPi =
    type === "product-intent" && itemId === scenario.selectedProductIntentId;
  const pi = type === "product-intent" ? getProductIntent(itemId) : undefined;
  const dc = type === "discovery-case" ? getDiscoveryCase(itemId) : undefined;
  const ri = type === "release-intent" ? getReleaseIntent(itemId) : undefined;
  const linkedPi = ri ? getProductIntent(ri.sourceProductIntentId) : undefined;
  const linkedWorkOrders = ri
    ? getWorkOrdersForWorkbench(workbenchId).filter(
        (wo) => wo.orchestrationItemId === ri.sourceProductIntentId
      )
    : [];

  return (
    <div className="f-page">
      <Breadcrumb
        items={[
          { label: "Foundry", to: foundryHomePath() },
          ...(workshop
            ? [{ label: workshop.name, to: workshopHomePath(workshop.id) }]
            : []),
          ...(workbench
            ? [{ label: workbench.name, to: workbenchHomePath(workbench.id) }]
            : []),
          { label: "Orchestration", to: consolePath(workbenchId, "orchestration") },
          { label: itemId }
        ]}
      />
      <h1 className="f-page-title">
        {type}: <span className="f-tech">{itemId}</span>
      </h1>
      {pi ? <p className="f-page-subtitle">{pi.title}</p> : null}
      {dc ? <p className="f-page-subtitle">{dc.title}</p> : null}
      {ri ? <p className="f-page-subtitle">{ri.title}</p> : null}
      {isScenarioPi ? (
        <BuildTrackPanel />
      ) : ri ? (
        <div className="f-grid f-grid--2">
          <section className="f-card">
            <h3>Release Intent Summary</h3>
            <div className="f-inline-row">
              <StatusBadge tone={toneForRiskLevel(ri.riskLevel)}>
                {`${ri.riskLevel} risk`}
              </StatusBadge>
              <StatusBadge tone="info">{ri.stage}</StatusBadge>
              <StatusBadge tone="info">{ri.status}</StatusBadge>
            </div>
            <p className="f-meta-line">
              Target window: <span className="f-tech">{formatDateTime(ri.targetReleaseWindow)}</span>
            </p>
            <p className="f-meta-line">
              Owner: <span className="f-tech">{resolvePersonName(ri.owner)}</span>
            </p>
            {linkedPi ? (
              <p className="f-meta-line">
                Source PI:{" "}
                <Link
                  to={orchestrationItemPath(workbenchId, "product-intent", linkedPi.id)}
                  className="f-text-link"
                >
                  <span className="f-tech">{linkedPi.id}</span> {linkedPi.title}
                </Link>
              </p>
            ) : null}
          </section>
          <section className="f-card">
            <h3>Linked Build Queue</h3>
            <ul className="f-list">
              {linkedWorkOrders.map((wo) => (
                <li key={wo.id}>
                  <span className="f-tech">{wo.id}</span> {wo.title}
                  <div className="f-inline-row">
                    <StatusBadge tone="info">{wo.stage}</StatusBadge>
                    <StatusBadge tone={toneForWorkOrderStatus(wo.status)}>
                      {wo.status}
                    </StatusBadge>
                  </div>
                </li>
              ))}
              {linkedWorkOrders.length === 0 ? (
                <li>No linked work orders for this release intent.</li>
              ) : null}
            </ul>
          </section>
        </div>
      ) : (
        <div className="f-card">
          <p>Orchestration item detail view.</p>
          {type === "product-intent" ? (
            <ul className="f-list">
              {getPrioritizedWorkOrders().map((wo) => (
                <li key={wo.id}>
                  <span className="f-tech">{wo.id}</span> {wo.title}
                </li>
              ))}
            </ul>
          ) : null}
        </div>
      )}
    </div>
  );
}

export function TeamMemberDetail() {
  const { workbenchId, memberId } = useParams<{
    workbenchId: string;
    memberId: string;
  }>();

  if (!workbenchId || !memberId) {
    return null;
  }

  const workbench = getWorkbench(workbenchId);
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const team = getWorkbenchTeam(workbenchId);
  const allMembers = team
    ? [...team.productManagers, ...team.developers, ...team.qaPeople]
    : [];
  const member = allMembers.find((p) => p.id === memberId);
  const profile = getTeamMemberProfile(memberId);
  const memberSessions = getWorkspaceSessionsForWorkbench(workbenchId).filter((session) =>
    session.ownerId === memberId
  );
  const profileSessions = profile
    ? profile.activeSessionIds
        .map((sessionId) => getWorkspaceSession(sessionId))
        .filter((session): session is NonNullable<typeof session> => Boolean(session))
    : [];
  const sessionsById = new Map(
    [...memberSessions, ...profileSessions].map((session) => [session.id, session])
  );
  const sessions = Array.from(sessionsById.values()).sort(
    (a, b) =>
      new Date(b.lastUpdatedAt).getTime() - new Date(a.lastUpdatedAt).getTime()
  );
  const openWorkOrders = profile
    ? profile.openWorkOrderIds
        .map((workOrderId) => getWorkOrder(workOrderId))
        .filter((wo): wo is NonNullable<typeof wo> => Boolean(wo))
    : [];
  const recentActivity = profile
    ? getActivityByIds(profile.recentActivityEventIds)
    : getActivityForWorkbench(workbenchId).filter((event) => event.actorId === memberId);

  return (
    <div className="f-page">
      <Breadcrumb
        items={[
          { label: "Foundry", to: foundryHomePath() },
          ...(workshop
            ? [{ label: workshop.name, to: workshopHomePath(workshop.id) }]
            : []),
          ...(workbench
            ? [{ label: workbench.name, to: workbenchHomePath(workbench.id) }]
            : []),
          { label: "Team", to: consolePath(workbenchId, "team") },
          { label: member?.name ?? memberId }
        ]}
      />
      <h1 className="f-page-title">Team Member Profile</h1>
      {member ? (
        <div className="f-grid">
          <section className="f-card">
            <h3>{member.name}</h3>
            <div className="f-inline-row">
              <StatusBadge tone="info">{member.role}</StatusBadge>
              {profile ? (
                <StatusBadge
                  tone={profile.capacityPercent > 90 ? "warning" : "success"}
                >
                  {`${profile.capacityPercent}% capacity`}
                </StatusBadge>
              ) : null}
            </div>
            <p className="f-meta-line">{profile?.headline ?? "Role profile pending enrichment."}</p>
            {profile ? (
              <p className="f-meta-line">
                {profile.location} • {profile.timezone}
              </p>
            ) : null}
            {profile?.skills.length ? (
              <>
                <h4 className="f-subtitle">Skills</h4>
                <ul className="f-list">
                  {profile.skills.map((skill) => (
                    <li key={skill}>
                      <span className="f-tech">{skill}</span>
                    </li>
                  ))}
                </ul>
              </>
            ) : null}
          </section>
          <div className="f-grid f-grid--2">
            <section className="f-card">
              <h3>Active Sessions</h3>
              <ul className="f-list">
                {sessions.map((session) => (
                  <li key={session.id}>
                    <Link
                      to={workspaceSessionPath(workbenchId, session.id)}
                      className="f-text-link"
                    >
                      <span className="f-session-inline-icon" aria-hidden="true">
                        {SESSION_ICON}
                      </span>{" "}
                      <span className="f-tech">{session.id}</span> {session.title}
                    </Link>
                    <p className="f-meta-line">
                      {session.workspaceType} • updated{" "}
                      <span className="f-tech">{formatDateTime(session.lastUpdatedAt)}</span>
                    </p>
                  </li>
                ))}
                {sessions.length === 0 ? <li>No active sessions linked.</li> : null}
              </ul>
            </section>
            <section className="f-card">
              <h3>Open Work Orders</h3>
              <ul className="f-list">
                {openWorkOrders.map((wo) => (
                  <li key={wo.id}>
                    <span className="f-tech">{wo.id}</span> {wo.title}
                    <div className="f-inline-row">
                      <StatusBadge tone={toneForWorkOrderStatus(wo.status)}>
                        {wo.status}
                      </StatusBadge>
                      <StatusBadge tone="info">{wo.stage}</StatusBadge>
                    </div>
                  </li>
                ))}
                {openWorkOrders.length === 0 ? (
                  <li>No explicit open work-order links in profile data.</li>
                ) : null}
              </ul>
            </section>
          </div>
          <section className="f-card">
            <h3>Recent Contributions</h3>
            <ul className="f-list">
              {recentActivity.map((event) => (
                <li key={event.id}>
                  <div className="f-inline-row">
                    <StatusBadge tone="info">{event.track}</StatusBadge>
                    <span className="f-tech">{formatDateTime(event.occurredAt)}</span>
                  </div>
                  <p className="f-meta-line">{event.action}</p>
                  <p className="f-meta-line">{event.summary}</p>
                </li>
              ))}
              {recentActivity.length === 0 ? <li>No recorded contributions yet.</li> : null}
            </ul>
          </section>
        </div>
      ) : (
        <div className="f-card">
          <p>Member not found.</p>
        </div>
      )}
    </div>
  );
}

export function WorkspaceSessionDetail() {
  const { workbenchId, sessionId } = useParams<{
    workbenchId: string;
    sessionId: string;
  }>();
  const resolvedWorkbenchId = workbenchId ?? "";
  const resolvedSessionId = sessionId ?? "";
  const workbench = getWorkbench(resolvedWorkbenchId);
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const session = getWorkspaceSession(resolvedSessionId);
  const linkedWorkOrders = session ? getWorkspaceSessionOwnedWorkOrders(session.id) : [];
  const sessionPod = session ? getSessionCoderPod(session.id) : undefined;
  const sessionAgents = session ? getSessionEmployedAgents(session.id) : undefined;
  const usageWindows = getSessionAgentWindows();
  const [selectedAgentWindow, setSelectedAgentWindow] = useState(
    usageWindows[0]?.id ?? "all"
  );
  const [selectedAgentId, setSelectedAgentId] = useState<string | null>(null);
  const [isAgentLogOpen, setIsAgentLogOpen] = useState(false);
  const windowedAgentUsage = session
    ? getSessionAgentUsage(selectedAgentWindow, session.id)
    : undefined;
  const tokenUsage = session ? getSessionTokenUsage(session.id) : undefined;
  const activityTypes = getSessionActivityEventTypes();
  const allActivityTypeIds = useMemo(
    () => activityTypes.map((type) => type.id),
    [activityTypes]
  );
  const [selectedActivityTypes, setSelectedActivityTypes] = useState(allActivityTypeIds);
  const selectedActivityTypeCount = selectedActivityTypes.length;
  const activityFilterStatusLabel =
    selectedActivityTypeCount === activityTypes.length
      ? "All event types"
      : selectedActivityTypeCount === 0
        ? "None selected"
        : `${selectedActivityTypeCount} selected`;
  const isActivityFilterActive =
    selectedActivityTypeCount > 0 && selectedActivityTypeCount < activityTypes.length;
  const sessionActivity = session
    ? getSessionActivity(session.id, { eventTypes: selectedActivityTypes })
    : [];
  const activityTypeLabelById = useMemo(
    () =>
      new Map(activityTypes.map((activityType) => [activityType.id, activityType.label])),
    [activityTypes]
  );
  const visibleAgents = windowedAgentUsage?.agents ?? [];
  const activeAgentId =
    selectedAgentId && visibleAgents.some((agent) => agent.agentId === selectedAgentId)
      ? selectedAgentId
      : visibleAgents[0]?.agentId ?? null;
  const activeAgent = visibleAgents.find((agent) => agent.agentId === activeAgentId);
  const activeAgentUsageLog = useMemo(() => {
    if (!activeAgentId) {
      return [];
    }
    return getAgentUsageLog(activeAgentId).filter(
      (entry) => entry.workbenchId === resolvedWorkbenchId
    );
  }, [activeAgentId, resolvedWorkbenchId]);
  if (!workbenchId || !sessionId) {
    return null;
  }
  const elapsedMinutes = session
    ? Math.max(
        1,
        Math.round(
          (new Date(session.lastUpdatedAt).getTime() -
            new Date(session.startedAt).getTime()) /
            (60 * 1000)
        )
      )
    : 0;

  return (
    <div className="f-page">
      <Breadcrumb
        items={[
          { label: "Foundry", to: foundryHomePath() },
          ...(workshop
            ? [{ label: workshop.name, to: workshopHomePath(workshop.id) }]
            : []),
          ...(workbench
            ? [{ label: workbench.name, to: workbenchHomePath(workbench.id) }]
            : []),
          {
            label: "Workspaces",
            to: consolePath(workbenchId, "workspaces-overview")
          },
          { label: `${SESSION_ICON} Session ${sessionId}` }
        ]}
      />
      <h1 className="f-page-title">
        <span className="f-session-inline-icon" aria-hidden="true">
          {SESSION_ICON}
        </span>{" "}
        Workspace Session <span className="f-tech">{sessionId}</span>
      </h1>
      {session ? (
        <div className="f-grid">
          <section className="f-card">
            <h3>Session Overview</h3>
            <div className="f-session-kv-list">
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Status</span>
                <span className="f-tech f-session-kv-value">{session.status}</span>
              </p>
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Workspace type</span>
                <span className="f-tech f-session-kv-value">{session.workspaceType}</span>
              </p>
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Session owner</span>
                <Link to={teamMemberPath(workbenchId, session.ownerId)} className="f-text-link">
                  <span className="f-tech">{resolvePersonName(session.ownerId)}</span>
                </Link>
              </p>
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Started</span>
                <span className="f-tech f-session-kv-value">{formatDateTime(session.startedAt)}</span>
              </p>
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Last updated</span>
                <span className="f-tech f-session-kv-value">
                  {formatDateTime(session.lastUpdatedAt)}
                </span>
              </p>
              <p className="f-session-kv-row">
                <span className="f-session-kv-label">Elapsed</span>
                <span className="f-tech f-session-kv-value">{formatDuration(elapsedMinutes)}</span>
              </p>
            </div>
            <div className="f-inline-row">
              <a
                href={session.remoteIdeUrl}
                target="_blank"
                rel="noreferrer"
                className="f-text-link"
              >
                Launch IDE
              </a>
            </div>
          </section>
          <div className="f-session-layout">
            <div className="f-session-main">
              <section className="f-card">
                <h3>Linked Work Orders</h3>
                <div className="f-session-wo-grid">
                  {linkedWorkOrders.map((wo) => (
                    <Link
                      key={wo.id}
                      to={workOrderDetailPath(workbenchId, wo.id)}
                      className="f-card f-card-link f-session-wo-card"
                    >
                      <p className="f-session-wo-title">
                        <span className="f-tech">{wo.id}</span> {wo.title}
                      </p>
                      <div className="f-session-kv-list f-session-kv-list--compact">
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Status</span>
                          <span className="f-tech f-session-kv-value">{wo.status}</span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Stage</span>
                          <span className="f-tech f-session-kv-value">{wo.stage}</span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Elapsed</span>
                          <span className="f-tech f-session-kv-value">
                            {formatDuration(getElapsedWorkOrderMinutesInSession(wo, session))}
                          </span>
                        </p>
                      </div>
                    </Link>
                  ))}
                  {linkedWorkOrders.length === 0 ? (
                    <div className="f-card f-card--nested">
                      <p>No linked work orders for this session.</p>
                    </div>
                  ) : null}
                </div>
              </section>

              <section className="f-card">
                <h3>Coder Pod</h3>
                {sessionPod ? (
                  <div className="f-grid">
                    <div className="f-grid f-grid--2">
                      <section className="f-card f-card--nested">
                        <h4 className="f-subtitle">Active pod</h4>
                        <div className="f-session-kv-list">
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Pod id</span>
                            <span className="f-tech f-session-kv-value">{sessionPod.activePod.id}</span>
                          </p>
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Status</span>
                            <span className="f-tech f-session-kv-value">
                              {sessionPod.activePod.status}
                            </span>
                          </p>
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Provider</span>
                            <span className="f-tech f-session-kv-value">
                              {sessionPod.activePod.provider}
                            </span>
                          </p>
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Cluster</span>
                            <span className="f-tech f-session-kv-value">
                              {sessionPod.activePod.cluster}
                            </span>
                          </p>
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Namespace</span>
                            <span className="f-tech f-session-kv-value">
                              {sessionPod.activePod.namespace}
                            </span>
                          </p>
                          <p className="f-session-kv-row">
                            <span className="f-session-kv-label">Branch</span>
                            <span className="f-tech f-session-kv-value">
                              {sessionPod.activePod.workspaceBranch}
                            </span>
                          </p>
                        </div>
                        <div className="f-inline-row">
                          <a
                            href={sessionPod.activePod.monitoringUrl}
                            target="_blank"
                            rel="noreferrer"
                            className="f-text-link"
                          >
                            Open Monitoring
                          </a>
                        </div>
                      </section>
                      <section className="f-card f-card--nested">
                        <h4 className="f-subtitle">Pod details</h4>
                        <p className="f-meta-line">
                          Started:{" "}
                          <span className="f-tech">
                            {formatDateTime(sessionPod.activePod.startedAt)}
                          </span>
                        </p>
                        <p className="f-meta-line">
                          Heartbeat:{" "}
                          <span className="f-tech">
                            {formatDateTime(sessionPod.activePod.lastHeartbeatAt)}
                          </span>
                        </p>
                        <p className="f-meta-line">
                          Health:{" "}
                          <span className="f-tech">
                            {sessionPod.activePod.health.status} ({sessionPod.activePod.health.score}
                            )
                          </span>
                        </p>
                        <p className="f-meta-line">
                          Resources:{" "}
                          <span className="f-tech">
                            {sessionPod.activePod.resources.cpuCores} CPU /{" "}
                            {sessionPod.activePod.resources.memoryGiB} GiB RAM /{" "}
                            {sessionPod.activePod.resources.ephemeralStorageGiB} GiB storage
                          </span>
                        </p>
                        <p className="f-meta-line">
                          Health issues:{" "}
                          <span className="f-tech">
                            {sessionPod.activePod.health.issues.length > 0
                              ? sessionPod.activePod.health.issues.join(", ")
                              : "none"}
                          </span>
                        </p>
                      </section>
                    </div>
                    <section className="f-card f-card--nested">
                      <h4 className="f-subtitle">Pod history</h4>
                      <ul className="f-list">
                        {sessionPod.podHistory.map((pod) => (
                          <li key={pod.id}>
                            <span className="f-tech">{pod.id}</span> {pod.reason}
                            <p className="f-meta-line">
                              Status: <span className="f-tech">{pod.status}</span>
                            </p>
                            <p className="f-meta-line">
                              Window:{" "}
                              <span className="f-tech">
                                {formatDateTime(pod.startedAt)} - {formatDateTime(pod.endedAt)}
                              </span>
                            </p>
                          </li>
                        ))}
                        {sessionPod.podHistory.length === 0 ? (
                          <li>No historical pod records.</li>
                        ) : null}
                      </ul>
                    </section>
                  </div>
                ) : (
                  <p>No coder pod data recorded for this session.</p>
                )}
              </section>

              <section className="f-card">
                <h3>Employed Agents</h3>
                {sessionAgents ? (
                  <>
                    <label className="f-meta-line" htmlFor="session-agent-window">
                      Window
                    </label>
                    <select
                      id="session-agent-window"
                      className="f-session-select"
                      value={selectedAgentWindow}
                      onChange={(event) => setSelectedAgentWindow(event.target.value)}
                    >
                      {usageWindows.map((window) => (
                        <option key={window.id} value={window.id}>
                          {window.label}
                        </option>
                      ))}
                    </select>
                    <p className="f-meta-line">
                      Range:{" "}
                      <span className="f-tech">
                        {windowedAgentUsage
                          ? `${formatDateTime(windowedAgentUsage.from)} - ${formatDateTime(windowedAgentUsage.to)}`
                          : "No data"}
                      </span>
                    </p>
                    <div className="f-agent-card-grid">
                      {visibleAgents.map((agent) => (
                        <button
                          key={agent.agentId}
                          type="button"
                          className={`f-agent-card${
                            activeAgentId === agent.agentId ? " f-agent-card--active" : ""
                          }`}
                          onClick={() => {
                            setSelectedAgentId(agent.agentId);
                            setIsAgentLogOpen(true);
                          }}
                          aria-pressed={activeAgentId === agent.agentId}
                        >
                          <p className="f-agent-card-title f-tech">{agent.agentName}</p>
                          <p className="f-agent-card-meta">
                            <span className="f-tech">{agent.invocationCount}</span> invocations
                          </p>
                          <p className="f-agent-card-meta">
                            <span className="f-tech">{agent.skills.length}</span> skills in this window
                          </p>
                          <p className="f-agent-card-meta">
                            Top skills:{" "}
                            <span className="f-tech">
                              {agent.skills
                                .slice(0, 2)
                                .map((skill) => `${skill.skillName} (${skill.invocationCount})`)
                                .join(", ")}
                            </span>
                          </p>
                        </button>
                      ))}
                    </div>
                    {visibleAgents.length === 0 ? (
                      <p className="f-meta-line">No employed agents recorded in this window.</p>
                    ) : null}
                    <p className="f-meta-line">
                      Click an agent card to open a detailed usage log dialog.
                    </p>
                  </>
                ) : (
                  <p>No employed agent data recorded for this session.</p>
                )}
              </section>

              <section className="f-card">
                <h3>Token Usage</h3>
                {tokenUsage ? (
                  <div className="f-grid">
                    <section className="f-card f-card--nested">
                      <h4 className="f-subtitle">Overview</h4>
                      <div className="f-session-kv-list f-session-kv-list--compact">
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Currency</span>
                          <span className="f-session-kv-value f-tech">{tokenUsage.currency}</span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Total cost</span>
                          <span className="f-session-kv-value f-tech">
                            {formatCurrencyUsd(tokenUsage.totals.totalCostUsd)}
                          </span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Total tokens</span>
                          <span className="f-session-kv-value f-tech">
                            {formatTokenCount(tokenUsage.totals.totalTokens)}
                          </span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Input / output</span>
                          <span className="f-session-kv-value f-tech">
                            {formatTokenCount(tokenUsage.totals.inputTokens)} /{" "}
                            {formatTokenCount(tokenUsage.totals.outputTokens)}
                          </span>
                        </p>
                        <p className="f-session-kv-row">
                          <span className="f-session-kv-label">Cache read / write</span>
                          <span className="f-session-kv-value f-tech">
                            {formatTokenCount(tokenUsage.totals.cacheReadTokens)} /{" "}
                            {formatTokenCount(tokenUsage.totals.cacheWriteTokens)}
                          </span>
                        </p>
                      </div>
                      <h4 className="f-subtitle">Tokens per day</h4>
                      <p className="f-meta-line">
                        Peak:{" "}
                        <span className="f-tech">
                          {formatCompactTokenCount(
                            Math.max(...tokenUsage.daily.map((point) => point.totalTokens), 0)
                          )}
                        </span>
                      </p>
                      <TokenUsageTimeline daily={tokenUsage.daily} />
                      <ul className="f-list f-list--plain f-token-daily-log">
                        {tokenUsage.daily.slice().reverse().map((point) => (
                          <li key={`${point.date}-daily`} className="f-token-daily-log-item">
                            <span className="f-tech">
                              {new Date(point.date).toLocaleDateString("en-IN", {
                                month: "short",
                                day: "2-digit"
                              })}
                            </span>
                            <span className="f-tech">{formatTokenCount(point.totalTokens)} tokens</span>
                            <span className="f-tech">{formatCurrencyUsd(point.totalCostUsd)}</span>
                          </li>
                        ))}
                      </ul>
                    </section>
                    <div className="f-grid f-grid--2">
                      <TokenCostBars
                        title="By model (cost)"
                        items={tokenUsage.models
                          .slice()
                          .sort((a, b) => b.totalCostUsd - a.totalCostUsd)
                          .map((model) => ({
                          id: model.modelId,
                          label: `${model.modelId} (${formatPercent(
                            (model.totalCostUsd / Math.max(tokenUsage.totals.totalCostUsd, 0.001)) * 100
                          )})`,
                          totalCostUsd: model.totalCostUsd,
                          detail: `Tokens: ${formatTokenCount(
                            model.inputTokens +
                              model.outputTokens +
                              model.cacheReadTokens +
                              model.cacheWriteTokens
                          )}`,
                          secondaryDetail: `In: ${formatTokenCount(model.inputTokens)} • Out: ${formatTokenCount(
                            model.outputTokens
                          )} • CR: ${formatTokenCount(model.cacheReadTokens)} • CW: ${formatTokenCount(
                            model.cacheWriteTokens
                          )}`
                        }))}
                      />
                      <TokenCostBars
                        title="By agent (cost)"
                        items={tokenUsage.agents
                          .slice()
                          .sort((a, b) => b.totalCostUsd - a.totalCostUsd)
                          .map((agent) => ({
                          id: agent.agentId,
                          label: `${agent.agentId} (${formatPercent(
                            (agent.totalCostUsd / Math.max(tokenUsage.totals.totalCostUsd, 0.001)) * 100
                          )})`,
                          totalCostUsd: agent.totalCostUsd,
                          detail: `Invocations: ${agent.invocationCount}`,
                          secondaryDetail: `Tokens: ${formatTokenCount(
                            agent.inputTokens + agent.outputTokens
                          )}`
                        }))}
                      />
                    </div>
                  </div>
                ) : (
                  <p>No token usage data recorded for this session.</p>
                )}
              </section>
            </div>
            <aside className="f-session-activity-rail">
              <section className="f-card">
                <h3>Session Activity</h3>
                <p className="f-meta-line">Filter by event types</p>
                <details className="f-session-activity-filter">
                  <summary
                    className={`f-session-activity-filter-trigger${
                      isActivityFilterActive ? " f-session-activity-filter-trigger--active" : ""
                    }`}
                    aria-label="Filter session activity event types"
                  >
                    <span className="f-session-activity-filter-trigger-main">
                      <svg
                        className="f-session-activity-filter-icon"
                        width="14"
                        height="14"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                        aria-hidden="true"
                        focusable="false"
                      >
                        <path
                          d="M3 6H21M7 12H17M10 18H14"
                          stroke="currentColor"
                          strokeWidth="2"
                          strokeLinecap="round"
                        />
                      </svg>
                      <span>Session Activity</span>
                    </span>
                    <span className="f-session-activity-filter-count">
                      {activityFilterStatusLabel}
                    </span>
                  </summary>
                  <div className="f-session-activity-filter-menu">
                    <div className="f-session-activity-filter-menu-header">Event types</div>
                    <div className="f-inline-row">
                      <button
                        type="button"
                        className="f-button f-button--ghost"
                        onClick={() => setSelectedActivityTypes(allActivityTypeIds)}
                      >
                        Select all
                      </button>
                      <button
                        type="button"
                        className="f-button f-button--ghost"
                        onClick={() => setSelectedActivityTypes([])}
                      >
                        Clear all
                      </button>
                    </div>
                    <div className="f-session-activity-filter-separator" />
                    <div className="f-session-activity-filter-options">
                      {activityTypes.map((eventType) => {
                        const isSelected = selectedActivityTypes.includes(eventType.id);
                        return (
                          <label
                            key={eventType.id}
                            className="f-session-activity-filter-option"
                          >
                            <input
                              type="checkbox"
                              className="f-session-activity-filter-checkbox"
                              checked={isSelected}
                              onChange={(event) => {
                                setSelectedActivityTypes((current) => {
                                  if (event.target.checked) {
                                    if (current.includes(eventType.id)) {
                                      return current;
                                    }
                                    return [...current, eventType.id];
                                  }
                                  return current.filter((id) => id !== eventType.id);
                                });
                              }}
                            />
                            <span>{eventType.label}</span>
                          </label>
                        );
                      })}
                    </div>
                  </div>
                </details>
                <p className="f-meta-line">
                  Showing {selectedActivityTypeCount} of {activityTypes.length} event types.
                </p>
                <ul className="f-list">
                  {sessionActivity.map((event) => (
                    <li key={event.id}>
                      <p className="f-meta-line">
                        <span className="f-tech">{formatDateTime(event.occurredAt)}</span>
                      </p>
                      <p className="f-meta-line">
                        <span className="f-tech">
                          {activityTypeLabelById.get(event.eventType) ?? event.eventType}
                        </span>
                      </p>
                      <p className="f-meta-line">{event.summary}</p>
                      <p className="f-meta-line">
                        Actor: <span className="f-tech">{resolvePersonName(event.actorId)}</span>
                      </p>
                    </li>
                  ))}
                  {sessionActivity.length === 0 ? (
                    <li>No activity for selected event types.</li>
                  ) : null}
                </ul>
              </section>
            </aside>
          </div>
          {isAgentLogOpen && activeAgent ? (
            <div
              className="f-dialog-overlay f-dialog-overlay--agent-log"
              role="presentation"
              onClick={() => setIsAgentLogOpen(false)}
            >
              <section
                className="f-dialog-content f-agent-log-dialog"
                role="dialog"
                aria-modal="true"
                aria-label={`Agent usage log ${activeAgent.agentName}`}
                onClick={(event) => event.stopPropagation()}
              >
                <div className="f-agent-log-header">
                  <h4 className="f-dialog-title">
                    Agent Usage Log — <span className="f-tech">{activeAgent.agentName}</span>
                  </h4>
                  <button
                    type="button"
                    className="f-button f-button--ghost"
                    onClick={() => setIsAgentLogOpen(false)}
                  >
                    Close
                  </button>
                </div>
                <p className="f-dialog-description">
                  Chronological session log format (timestamp, level, event, context).
                </p>
                <div className="f-agent-log-terminal">
                  {activeAgentUsageLog.map((entry) => (
                    <div key={`${entry.sessionId}-${entry.agentId}`} className="f-agent-log-block">
                      <p className="f-agent-log-line">
                        <span className="f-tech f-agent-log-ts">
                          {formatLogTimestamp(entry.from)}
                        </span>{" "}
                        <span className="f-agent-log-level">INFO</span>{" "}
                        <span className="f-tech">session.start</span>{" "}
                        <Link
                          to={workspaceSessionPath(entry.workbenchId, entry.sessionId)}
                          className="f-text-link"
                          onClick={() => setIsAgentLogOpen(false)}
                        >
                                  <span className="f-session-inline-icon" aria-hidden="true">
                                    {SESSION_ICON}
                                  </span>{" "}
                          <span className="f-tech">{entry.sessionId}</span>
                        </Link>{" "}
                        owner=<span className="f-tech">{resolvePersonName(entry.ownerId)}</span>
                      </p>
                      <p className="f-agent-log-line">
                        <span className="f-tech f-agent-log-ts">
                          {formatLogTimestamp(entry.to)}
                        </span>{" "}
                        <span className="f-agent-log-level">INFO</span>{" "}
                        <span className="f-tech">agent.summary</span>{" "}
                        invocations=<span className="f-tech">{entry.invocationCount}</span> skills=
                        <span className="f-tech">{entry.skills.length}</span> session=
                        <span className="f-tech">{entry.sessionTitle}</span>
                      </p>
                      {entry.skills.map((skill) => (
                        <p key={skill.skillId} className="f-agent-log-line">
                          <span className="f-tech f-agent-log-ts">
                            {formatLogTimestamp(entry.to)}
                          </span>{" "}
                          <span className="f-agent-log-level">INFO</span>{" "}
                          <span className="f-tech">skill.invocation</span>{" "}
                          skill=<span className="f-tech">{skill.skillName}</span> count=
                          <span className="f-tech">{skill.invocationCount}</span>
                        </p>
                      ))}
                      <p className="f-agent-log-line">
                        <span className="f-tech f-agent-log-ts">
                          {formatLogTimestamp(entry.to)}
                        </span>{" "}
                        <span className="f-agent-log-level">INFO</span>{" "}
                        <span className="f-tech">session.end</span>{" "}
                        <span className="f-session-inline-icon" aria-hidden="true">
                          {SESSION_ICON}
                        </span>{" "}
                        <span className="f-tech">{entry.sessionId}</span>
                      </p>
                    </div>
                  ))}
                  {activeAgentUsageLog.length === 0 ? (
                    <p className="f-agent-log-line">
                      <span className="f-tech f-agent-log-ts">{new Date().toISOString()}</span>{" "}
                      <span className="f-agent-log-level">WARN</span>{" "}
                      <span className="f-tech">agent.log.empty</span> no historical sessions in this
                      workbench.
                    </p>
                  ) : null}
                </div>
              </section>
            </div>
          ) : null}
        </div>
      ) : (
        <div className="f-card">
          <p>Session not found for this workbench.</p>
        </div>
      )}
    </div>
  );
}
