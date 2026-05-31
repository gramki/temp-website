import { Link } from "react-router-dom";
import { tenant, workshops } from "@/lib/data";
import { workshopHomePath } from "@/lib/routes";
import "@/foundry-ui/theme/components.css";

export function FoundryHome() {
  return (
    <div className="f-page">
      <header className="f-page-header">
        <h1 className="f-page-title">Foundry Home</h1>
        <p className="f-page-subtitle">
          Tenant: {tenant.name} — select a workshop to continue.
        </p>
      </header>
      <div className="f-grid f-grid--2">
        {workshops.map((workshop) => (
          <Link
            key={workshop.id}
            to={workshopHomePath(workshop.id)}
            className="f-card f-card-link"
          >
            <h3>{workshop.name}</h3>
            <p>
              {workshop.workbenchIds.length} workbench
              {workshop.workbenchIds.length === 1 ? "" : "es"}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
