import { Link, useParams } from "react-router-dom";
import { Breadcrumb } from "@/foundry-ui/components/ConsolePage";
import { StatusBadge } from "@/foundry-ui/components";
import {
  getTasksForWorkOrder,
  getWorkbench,
  getWorkOrder,
  getWorkshop,
  resolvePersonName
} from "@/lib/data";
import {
  consolePath,
  foundryHomePath,
  workshopHomePath,
  workbenchHomePath
} from "@/lib/routes";

function formatDateTime(isoTs: string) {
  return new Date(isoTs).toLocaleString("en-IN", {
    month: "short",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function toneForWorkOrderStatus(status: string) {
  if (status === "blocked") return "blocked" as const;
  if (status === "in-progress") return "info" as const;
  if (status === "queued") return "warning" as const;
  return "success" as const;
}

export function WorkOrderDetail() {
  const { workbenchId, workOrderId } = useParams<{
    workbenchId: string;
    workOrderId: string;
  }>();

  if (!workbenchId || !workOrderId) {
    return null;
  }

  const workbench = getWorkbench(workbenchId);
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const workOrder = getWorkOrder(workOrderId);
  const tasks = workOrder ? getTasksForWorkOrder(workOrder.id) : [];

  return (
    <div className="f-page">
      <Breadcrumb
        items={[
          { label: "Foundry", to: foundryHomePath() },
          ...(workshop ? [{ label: workshop.name, to: workshopHomePath(workshop.id) }] : []),
          ...(workbench ? [{ label: workbench.name, to: workbenchHomePath(workbench.id) }] : []),
          { label: "Workspaces", to: consolePath(workbenchId, "workspaces-overview") },
          { label: workOrderId }
        ]}
      />
      <h1 className="f-page-title">
        Work Order <span className="f-tech">{workOrderId}</span>
      </h1>
      {workOrder ? (
        <div className="f-grid">
          <section className="f-card">
            <h3>{workOrder.title}</h3>
            <div className="f-inline-row">
              <StatusBadge tone={toneForWorkOrderStatus(workOrder.status)}>
                {workOrder.status}
              </StatusBadge>
              <StatusBadge tone="info">{workOrder.stage}</StatusBadge>
              <StatusBadge tone="info">{workOrder.orchestrationItemType}</StatusBadge>
            </div>
            <p className="f-meta-line">
              Owner: <span className="f-tech">{resolvePersonName(workOrder.owner)}</span>
            </p>
            <p className="f-meta-line">
              Branch: <span className="f-tech">{workOrder.branch}</span>
            </p>
            <p className="f-meta-line">
              Created: <span className="f-tech">{formatDateTime(workOrder.createdAt)}</span>
            </p>
            <p className="f-meta-line">
              Updated: <span className="f-tech">{formatDateTime(workOrder.updatedAt)}</span>
            </p>
          </section>
          <section className="f-card">
            <h3>Task Summary</h3>
            <ul className="f-list">
              {tasks.map((task) => (
                <li key={task.id}>
                  <span className="f-tech">{task.id}</span> {task.title}
                  <div className="f-inline-row">
                    <StatusBadge tone={toneForWorkOrderStatus(task.status)}>
                      {task.status}
                    </StatusBadge>
                    <StatusBadge tone="info">{task.kind}</StatusBadge>
                  </div>
                </li>
              ))}
              {tasks.length === 0 ? <li>No tasks are linked to this work order yet.</li> : null}
            </ul>
          </section>
          <section className="f-card">
            <p className="f-meta-line">
              This page is intentionally minimal for session card click-through and will be expanded
              in the next routing depth pass.
            </p>
            <div className="f-inline-row">
              <Link to={consolePath(workbenchId, "workspaces-overview")} className="f-text-link">
                Back to workspaces
              </Link>
            </div>
          </section>
        </div>
      ) : (
        <div className="f-card">
          <p>Work order not found for this workbench.</p>
        </div>
      )}
    </div>
  );
}
