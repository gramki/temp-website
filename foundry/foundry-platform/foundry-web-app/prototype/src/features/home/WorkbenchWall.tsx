import { useEffect, useRef, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { StatusBadge } from "@/foundry-ui/components";
import {
  getActivityForWorkbench,
  getIntentsForWorkbench,
  getScenarioIntent,
  getTeamMemberProfile,
  getWorkbench,
  getWorkOrdersForWorkbench,
  getWorkshop,
  resolvePersonName,
  scenario
} from "@/lib/data";
import { consolePath, orchestrationItemPath, workshopHomePath } from "@/lib/routes";

const ACTIVITY_BATCH_SIZE = 8;

function formatActivityTime(isoTs: string): string {
  const nowMs = Date.now();
  const eventMs = new Date(isoTs).getTime();
  const diffMs = Math.max(0, nowMs - eventMs);
  const minuteMs = 60 * 1000;
  const hourMs = 60 * minuteMs;
  const dayMs = 24 * hourMs;

  if (diffMs < minuteMs) {
    return "Just now";
  }
  if (diffMs < hourMs) {
    return `${Math.floor(diffMs / minuteMs)}m ago`;
  }
  if (diffMs < dayMs) {
    return `${Math.floor(diffMs / hourMs)}h ago`;
  }
  if (diffMs < 2 * dayMs) {
    return "Yesterday";
  }
  if (diffMs < 7 * dayMs) {
    return `${Math.floor(diffMs / dayMs)}d ago`;
  }
  return new Date(isoTs).toLocaleDateString("en-IN", {
    month: "short",
    day: "2-digit"
  });
}

function getInitials(name: string): string {
  return name
    .split(" ")
    .map((part) => part[0] ?? "")
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

function humanizeIdentifier(value: string): string {
  return value
    .split("-")
    .filter(Boolean)
    .map((part) => part[0]?.toUpperCase() + part.slice(1))
    .join(" ");
}

export function WorkbenchWall() {
  const { workbenchId } = useParams<{ workbenchId: string }>();
  const workbench = workbenchId ? getWorkbench(workbenchId) : undefined;
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const intents = workbenchId ? getIntentsForWorkbench(workbenchId) : [];
  const workOrders = workbenchId ? getWorkOrdersForWorkbench(workbenchId) : [];
  const activity = workbenchId ? getActivityForWorkbench(workbenchId) : [];
  const [visibleActivityCount, setVisibleActivityCount] = useState(ACTIVITY_BATCH_SIZE);
  const activitySentinelRef = useRef<HTMLDivElement | null>(null);
  const isScenarioWorkbench = workbenchId === scenario.defaultWorkbenchId;
  const scenarioIntent = isScenarioWorkbench ? getScenarioIntent() : undefined;
  const productDescription = intents[0]?.domainDescription;
  const activeWorkOrderCount = workOrders.filter(
    (wo) => wo.status !== "completed"
  ).length;
  const dueTodayItems = workbenchId
    ? workOrders
        .filter((workOrder) => workOrder.status !== "completed")
        .sort(
          (a, b) =>
            new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime()
        )
        .slice(0, 6)
        .map((workOrder) => {
          const workspace = workOrder.stage
            ? humanizeIdentifier(workOrder.stage)
            : "Workbench";
          const resolvedPersonName = resolvePersonName(workOrder.owner);
          const person =
            resolvedPersonName === workOrder.owner
              ? humanizeIdentifier(workOrder.owner)
              : resolvedPersonName;
          return {
            ...workOrder,
            person,
            route: orchestrationItemPath(workbenchId, "work-order", workOrder.id),
            workspace
          };
        })
    : [];
  const visibleActivity = activity.slice(0, visibleActivityCount);
  const hasMoreActivity = visibleActivityCount < activity.length;

  useEffect(() => {
    setVisibleActivityCount(ACTIVITY_BATCH_SIZE);
  }, [workbenchId]);

  useEffect(() => {
    if (!hasMoreActivity) {
      return;
    }
    const sentinel = activitySentinelRef.current;
    if (!sentinel) {
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        const first = entries[0];
        if (!first?.isIntersecting) {
          return;
        }
        observer.unobserve(first.target);
        setVisibleActivityCount((current) =>
          Math.min(current + ACTIVITY_BATCH_SIZE, activity.length)
        );
      },
      { rootMargin: "160px 0px" }
    );

    observer.observe(sentinel);
    return () => observer.disconnect();
  }, [activity.length, hasMoreActivity, visibleActivityCount]);

  if (!workbench || !workshop) {
    return <p>Workbench not found.</p>;
  }

  return (
    <article className="f-wall">
      <header className="f-wall-header">
        <h2 className="f-console-title">{workbench.name}</h2>
        {productDescription ? (
          <p className="f-wall-description">{productDescription}</p>
        ) : null}
        <div className="f-inline-row">
          <Link to={workshopHomePath(workshop.id)} className="f-badge-link">
            <StatusBadge tone="info">{workshop.name}</StatusBadge>
          </Link>
          <StatusBadge tone="info">{workbench.slug}</StatusBadge>
          <StatusBadge tone="success">{`${activeWorkOrderCount} active WOs`}</StatusBadge>
        </div>
      </header>

      {intents.length > 0 ? (
        <div
          className="f-pi-badge-row"
          role="list"
          aria-label="Active product intents"
        >
          {intents.map((pi) => (
            <Link
              key={pi.id}
              to={orchestrationItemPath(workbench.id, "product-intent", pi.id)}
              className="f-pi-badge f-card-link"
              role="listitem"
            >
              <span className="f-tech">{pi.id}</span>
              <span>{pi.title}</span>
              <StatusBadge tone="info">{pi.stage}</StatusBadge>
            </Link>
          ))}
        </div>
      ) : null}

      {scenarioIntent ? (
        <section className="f-card f-wall-highlight">
          <h3>Build Track Focus</h3>
          <p>{scenarioIntent.title}</p>
          <div className="f-inline-row">
            <StatusBadge tone="info">Build Track</StatusBadge>
            <StatusBadge tone="warning">2 Prioritized WOs</StatusBadge>
          </div>
          <div className="f-inline-row">
            <Link
              to={orchestrationItemPath(
                workbench.id,
                "product-intent",
                scenarioIntent.id
              )}
              className="f-text-link"
            >
              View Product Intent
            </Link>
            <Link
              to={consolePath(workbench.id, "release-artifacts")}
              className="f-text-link"
            >
              Release Artifacts
            </Link>
          </div>
        </section>
      ) : null}

      <div className="f-grid f-grid--2">
        <section className="f-card">
          <h3>Due Today</h3>
          <ul className="f-list f-list--plain f-wall-task-list">
            {dueTodayItems.map((item) => (
              <li key={item.id}>
                <Link to={item.route} className="f-card-link f-wall-task-link">
                  <div className="f-wall-task-top">
                    <span className="f-tech">{item.id}</span>
                    <StatusBadge tone={item.status === "blocked" ? "blocked" : "info"}>
                      {item.status}
                    </StatusBadge>
                  </div>
                  <p className="f-wall-task-title">{item.title}</p>
                  <p className="f-wall-task-meta">
                    <span>{item.workspace} workspace</span>
                    <span>{item.person}</span>
                  </p>
                </Link>
              </li>
            ))}
            {dueTodayItems.length === 0 ? (
              <li>
                <span className="f-meta-line">
                  No work items due today for this workbench yet.
                </span>
              </li>
            ) : null}
          </ul>
        </section>
        <section className="f-card">
          <h3>Recent Activity</h3>
          <ul className="f-list f-list--plain f-wall-activity-list">
            {visibleActivity.map((event) => {
              const actorName = resolvePersonName(event.actorId);
              const profile = getTeamMemberProfile(event.actorId);
              const actorInitials = getInitials(actorName);
              return (
                <li key={event.id} className="f-wall-activity-item">
                  <div className="f-wall-activity-header">
                    <div className="f-wall-activity-title">
                      {profile?.avatarUrl ? (
                        <img
                          src={profile.avatarUrl}
                          alt=""
                          className="f-profile-avatar f-wall-activity-avatar"
                        />
                      ) : (
                        <span
                          className="f-profile-avatar f-profile-avatar--initials f-wall-activity-avatar"
                          aria-hidden="true"
                        >
                          {actorInitials}
                        </span>
                      )}
                      <div>
                        <p className="f-wall-activity-action">{event.action}</p>
                        <p className="f-wall-activity-actor">{actorName}</p>
                      </div>
                    </div>
                    <span className="f-tech f-wall-activity-time">
                      {formatActivityTime(event.occurredAt)}
                    </span>
                  </div>
                  <p className="f-meta-line">{event.summary}</p>
                  <p className="f-meta-line">
                    <span className="f-tech">
                      {event.track} · {event.entityType}: {event.entityId}
                    </span>
                  </p>
                </li>
              );
            })}
            {activity.length === 0 ? (
              <li>
                <span className="f-meta-line">
                  No cross-track activity recorded for this workbench yet.
                </span>
              </li>
            ) : null}
          </ul>
          {activity.length > 0 ? (
            <div
              ref={activitySentinelRef}
              className="f-wall-activity-sentinel"
              aria-hidden="true"
            />
          ) : null}
          {hasMoreActivity ? (
            <p className="f-meta-line f-wall-activity-loading">Loading more activity...</p>
          ) : null}
        </section>
      </div>
    </article>
  );
}
