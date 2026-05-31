import { Link } from "react-router-dom";
import { StatusBadge } from "@/foundry-ui/components";
import type { BadgeTone } from "@/foundry-ui/components/StatusBadge";
import {
  getGovernanceForIntent,
  getPrioritizedWorkOrders,
  getScenarioIntent,
  getTasksForWorkOrder,
  getWorkbench,
  getWorkbenchTeam,
  getWorkshop,
  scenario
} from "@/lib/data";
import { orchestrationItemPath } from "@/lib/routes";

type WorkOrderStatus = "completed" | "in-progress" | "queued" | "blocked";

function toneForWorkOrder(status: WorkOrderStatus): BadgeTone {
  if (status === "completed") return "success";
  if (status === "in-progress") return "info";
  if (status === "blocked") return "blocked";
  return "warning";
}

function toneForGovernance(
  verdict: "pass" | "review" | "fail",
  blockType: "none" | "soft" | "hard"
): BadgeTone {
  if (verdict === "pass") return "governance-pass";
  if (verdict === "fail") {
    return blockType === "hard" ? "governance-hard-block" : "governance-fail";
  }
  return blockType === "soft" ? "governance-soft-block" : "governance-review";
}

export function BuildTrackPanel() {
  const selectedIntent = getScenarioIntent();
  const selectedWorkshop = getWorkshop(scenario.defaultWorkshopId);
  const selectedWorkbench = getWorkbench(scenario.defaultWorkbenchId);

  if (!selectedIntent || !selectedWorkshop || !selectedWorkbench) {
    return <p>Build Track scenario data is misconfigured.</p>;
  }

  const prioritizedWorkOrders = getPrioritizedWorkOrders();
  const intentGovernanceVerdicts = getGovernanceForIntent(selectedIntent.id);
  const workbenchTeam = getWorkbenchTeam(selectedWorkbench.id);

  return (
    <section className="f-grid">
      <div className="f-card">
        <h3>Build Track — Two Work Orders</h3>
        <p>{scenario.notes}</p>
        <div className="f-inline-row">
          <StatusBadge tone="info">Build Track</StatusBadge>
          <StatusBadge tone="warning">
            {`Prioritized WOs: ${scenario.prioritizedWorkOrderIds.length}`}
          </StatusBadge>
        </div>
      </div>

      <div className="f-grid f-grid--2">
        <div className="f-card">
          <h3>
            Product Intent{" "}
            <Link
              to={orchestrationItemPath(
                selectedWorkbench.id,
                "product-intent",
                selectedIntent.id
              )}
              className="f-tech f-text-link"
            >
              {selectedIntent.id}
            </Link>
          </h3>
          <p>{selectedIntent.title}</p>
          <p className="f-meta-line">{selectedIntent.domainDescription}</p>
          <p className="f-meta-line">
            Stage: <span className="f-tech">{selectedIntent.stage}</span>
          </p>
          <p className="f-meta-line">
            {selectedWorkshop.name} / {selectedWorkbench.name}
          </p>
        </div>
        <div className="f-card">
          <h3>Workbench Team Snapshot</h3>
          {workbenchTeam ? (
            <ul className="f-list">
              <li>Product Managers: {workbenchTeam.productManagers.length}</li>
              <li>Developers: {workbenchTeam.developers.length}</li>
              <li>QA: {workbenchTeam.qaPeople.length}</li>
            </ul>
          ) : (
            <p>No team record.</p>
          )}
        </div>
      </div>

      <div className="f-card">
        <h3>Prioritized Work Orders</h3>
        <div className="f-grid f-grid--2">
          {prioritizedWorkOrders.map((workOrder) => {
            if (!workOrder) return null;
            const woTasks = getTasksForWorkOrder(workOrder.id);
            return (
              <article key={workOrder.id} className="f-card f-card--nested">
                <h3>
                  <span className="f-tech">{workOrder.id}</span> {workOrder.title}
                </h3>
                <div className="f-inline-row">
                  <StatusBadge
                    tone={toneForWorkOrder(workOrder.status as WorkOrderStatus)}
                  >
                    {workOrder.status}
                  </StatusBadge>
                  <StatusBadge tone="info">{workOrder.stage}</StatusBadge>
                </div>
                <p className="f-meta-line">
                  Owner: <span className="f-tech">{workOrder.owner}</span>
                </p>
                <h4 className="f-subtitle">Tasks</h4>
                <ul className="f-list">
                  {woTasks.map((task) => (
                    <li key={task.id}>
                      <span className="f-tech">{task.id}</span> {task.title} (
                      {task.status})
                    </li>
                  ))}
                </ul>
              </article>
            );
          })}
        </div>
      </div>

      <div className="f-card">
        <h3>Governance Context</h3>
        <ul className="f-list">
          {intentGovernanceVerdicts.map((verdict) => (
            <li key={verdict.id}>
              <div className="f-inline-row">
                <span className="f-tech">{verdict.id}</span>
                <StatusBadge
                  tone={toneForGovernance(
                    verdict.verdict as "pass" | "review" | "fail",
                    verdict.blockType as "none" | "soft" | "hard"
                  )}
                >
                  {verdict.verdict}
                </StatusBadge>
              </div>
              <p className="f-meta-line">{verdict.summary}</p>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
