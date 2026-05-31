import { StatusBadge } from "@/foundry-ui/components";
import scenarioData from "../../../mock-data/scenarios/buildTrackTwoWorkOrders.json";
import governanceData from "../../../mock-data/governance-verdicts.json";
import productIntentData from "../../../mock-data/product-intents.json";
import tasksData from "../../../mock-data/tasks.json";
import teamsData from "../../../mock-data/teams.json";
import traceabilityData from "../../../mock-data/traceability-links.json";
import workbenchData from "../../../mock-data/workbenches.json";
import workOrderData from "../../../mock-data/work-orders.json";
import workshopData from "../../../mock-data/workshops.json";

type BadgeTone =
  | "info"
  | "success"
  | "warning"
  | "error"
  | "blocked"
  | "governance-pass"
  | "governance-review"
  | "governance-fail"
  | "governance-soft-block"
  | "governance-hard-block";

type WorkOrderStatus = "completed" | "in-progress" | "queued" | "blocked";

function toneForWorkOrder(status: WorkOrderStatus): BadgeTone {
  if (status === "completed") {
    return "success";
  }
  if (status === "in-progress") {
    return "info";
  }
  if (status === "blocked") {
    return "blocked";
  }
  return "warning";
}

function toneForGovernance(
  verdict: "pass" | "review" | "fail",
  blockType: "none" | "soft" | "hard"
): BadgeTone {
  if (verdict === "pass") {
    return "governance-pass";
  }
  if (verdict === "fail") {
    return blockType === "hard" ? "governance-hard-block" : "governance-fail";
  }
  return blockType === "soft" ? "governance-soft-block" : "governance-review";
}

export function BuildView() {
  const scenario = scenarioData;
  const selectedIntent = productIntentData.productIntents.find(
    (intent) => intent.id === scenario.selectedProductIntentId
  );
  const selectedWorkshop = workshopData.workshops.find(
    (workshop) => workshop.id === scenario.defaultWorkshopId
  );
  const selectedWorkbench = workbenchData.workbenches.find(
    (workbench) => workbench.id === scenario.defaultWorkbenchId
  );

  if (!selectedIntent || !selectedWorkshop || !selectedWorkbench) {
    return (
      <section className="f-grid">
        <div className="f-card">
          <h3>Build Track Scenario Misconfigured</h3>
          <p>Selected scenario references missing workshop, workbench, or intent.</p>
          <StatusBadge tone="error">Data Error</StatusBadge>
        </div>
      </section>
    );
  }

  const prioritizedWorkOrders = scenario.prioritizedWorkOrderIds
    .map((workOrderId) =>
      workOrderData.workOrders.find((workOrder) => workOrder.id === workOrderId)
    )
    .filter((workOrder): workOrder is (typeof workOrderData.workOrders)[number] =>
      Boolean(workOrder)
    );

  const intentGovernanceVerdicts = traceabilityData.traceabilityLinks
    .filter(
      (link) =>
        link.type === "product-intent-to-governance-verdict" &&
        link.sourceId === selectedIntent.id
    )
    .map((link) =>
      governanceData.governanceVerdicts.find((verdict) => verdict.id === link.targetId)
    )
    .filter(
      (verdict): verdict is (typeof governanceData.governanceVerdicts)[number] =>
        Boolean(verdict)
    );

  const workbenchTeam = teamsData.workbenchTeams.find(
    (team) => team.workbenchId === selectedWorkbench.id
  );

  const taskListByWorkOrder = prioritizedWorkOrders.map((workOrder) => ({
    workOrder,
    tasks: tasksData.tasks.filter((task) => task.workOrderId === workOrder.id)
  }));

  return (
    <section className="f-grid">
      <div className="f-card">
        <h3>Build Track Priority Scenario</h3>
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
            Product Intent <span className="f-tech">{selectedIntent.id}</span>
          </h3>
          <p>{selectedIntent.title}</p>
          <p className="f-meta-line">{selectedIntent.domainDescription}</p>
          <p className="f-meta-line">
            Stage: <span className="f-tech">{selectedIntent.stage}</span>
          </p>
          <p className="f-meta-line">
            Workshop: {selectedWorkshop.name} | Workbench: {selectedWorkbench.name}
          </p>
        </div>
        <div className="f-card">
          <h3>Workbench Team Snapshot</h3>
          {workbenchTeam ? (
            <ul className="f-list">
              <li>Product Managers: {workbenchTeam.productManagers.length}</li>
              <li>Developers: {workbenchTeam.developers.length}</li>
              <li>QA: {workbenchTeam.qaPeople.length}</li>
              <li>Release Managers (shared): {workbenchTeam.releaseManagers.length}</li>
              <li>UX (shared): {workbenchTeam.uxPeople.length}</li>
            </ul>
          ) : (
            <p>No team record found for this workbench.</p>
          )}
        </div>
      </div>

      <div className="f-card">
        <h3>Prioritized Work Orders</h3>
        <div className="f-grid f-grid--2">
          {taskListByWorkOrder.map(({ workOrder, tasks }) => (
            <article key={workOrder.id} className="f-card f-card--nested">
              <h3>
                <span className="f-tech">{workOrder.id}</span> {workOrder.title}
              </h3>
              <div className="f-inline-row">
                <StatusBadge tone={toneForWorkOrder(workOrder.status as WorkOrderStatus)}>
                  {workOrder.status}
                </StatusBadge>
                <StatusBadge tone="info">{workOrder.stage}</StatusBadge>
              </div>
              <p className="f-meta-line">
                Owner: <span className="f-tech">{workOrder.owner}</span>
              </p>
              <p className="f-meta-line">
                Branch: <span className="f-tech">{workOrder.branch}</span>
              </p>
              <h4 className="f-subtitle">Tasks</h4>
              <ul className="f-list">
                {tasks.map((task) => (
                  <li key={task.id}>
                    <span className="f-tech">{task.id}</span> {task.title}
                  </li>
                ))}
              </ul>
            </article>
          ))}
        </div>
      </div>

      <div className="f-grid f-grid--2">
        <div className="f-card">
          <h3>Governance Verdicts</h3>
          {intentGovernanceVerdicts.length > 0 ? (
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
          ) : (
            <p>No governance verdicts linked yet.</p>
          )}
        </div>
        <div className="f-card">
          <h3>Traceability Focus</h3>
          <ul className="f-list">
            <li>
              Discovery -&gt; PI: <span className="f-tech">{selectedIntent.sourceDiscoveryCaseId}</span>
            </li>
            {prioritizedWorkOrders.map((workOrder) => (
              <li key={workOrder.id}>
                PI -&gt; WO: <span className="f-tech">{selectedIntent.id}</span> -&gt;{" "}
                <span className="f-tech">{workOrder.id}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
