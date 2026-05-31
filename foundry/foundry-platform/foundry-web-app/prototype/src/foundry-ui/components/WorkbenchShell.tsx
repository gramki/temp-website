import { NavLink, Outlet, useMatch, useParams } from "react-router-dom";
import { Breadcrumb } from "@/foundry-ui/components/ConsolePage";
import type { BreadcrumbItem } from "@/foundry-ui/components/ConsolePage";
import { CONSOLE_GROUPS } from "@/lib/navigation";
import {
  consolePath,
  foundryHomePath,
  workbenchHomePath,
  workshopHomePath
} from "@/lib/routes";
import { getWorkbench, getWorkshop } from "@/lib/data";
import { getConsoleById } from "@/lib/navigation";
import "@/foundry-ui/theme/components.css";

export function WorkbenchShell() {
  const { workbenchId, consoleId } = useParams<{
    workbenchId: string;
    consoleId?: string;
  }>();

  const wallMatch = useMatch({ path: "/workbenches/:workbenchId", end: true });

  if (!workbenchId) {
    return null;
  }

  const workbench = getWorkbench(workbenchId);
  const workshop = workbench ? getWorkshop(workbench.workshopId) : undefined;
  const consoleDef = consoleId ? getConsoleById(consoleId) : undefined;

  const breadcrumbItems: BreadcrumbItem[] = [
    { label: "Foundry", to: foundryHomePath() }
  ];
  if (workshop) {
    breadcrumbItems.push({
      label: workshop.name,
      to: workshopHomePath(workshop.id)
    });
  }
  if (workbench) {
    breadcrumbItems.push({
      label: workbench.name,
      to: workbenchHomePath(workbench.id)
    });
  }
  if (wallMatch) {
    breadcrumbItems.push({ label: "Wall" });
  } else if (consoleDef) {
    breadcrumbItems.push({ label: consoleDef.label });
  }

  return (
    <div className="f-workbench-layout">
      <aside className="f-side-nav" aria-label="Workbench navigation">
        <section className="f-side-nav-group f-side-nav-group--wall">
          <NavLink
            to={workbenchHomePath(workbenchId)}
            end
            className={({ isActive }) =>
              isActive
                ? "f-side-nav-link f-side-nav-link--wall f-side-nav-link--active"
                : "f-side-nav-link f-side-nav-link--wall"
            }
          >
            Wall
          </NavLink>
        </section>
        {CONSOLE_GROUPS.map((group) => (
          <section key={group.id} className="f-side-nav-group">
            <h3 className="f-side-nav-group-title">{group.label}</h3>
            <ul className="f-side-nav-list">
              {group.consoles.map((console) => (
                <li key={console.id}>
                  <NavLink
                    to={consolePath(workbenchId, console.id)}
                    className={({ isActive }) =>
                      isActive
                        ? "f-side-nav-link f-side-nav-link--active"
                        : "f-side-nav-link"
                    }
                  >
                    {console.label}
                  </NavLink>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </aside>
      <div className="f-workbench-main">
        <Breadcrumb items={breadcrumbItems} />
        <Outlet />
      </div>
    </div>
  );
}
