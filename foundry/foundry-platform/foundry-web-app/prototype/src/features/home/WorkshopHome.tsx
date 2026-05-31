import { Link, useParams } from "react-router-dom";
import { getWorkshop, workbenches } from "@/lib/data";
import { foundryHomePath, workbenchHomePath } from "@/lib/routes";
import { Breadcrumb } from "@/foundry-ui/components/ConsolePage";

export function WorkshopHome() {
  const { workshopId } = useParams<{ workshopId: string }>();
  const workshop = workshopId ? getWorkshop(workshopId) : undefined;

  if (!workshop) {
    return (
      <div className="f-page">
        <p>Workshop not found.</p>
        <Link to={foundryHomePath()}>Back to Foundry</Link>
      </div>
    );
  }

  const workshopBenches = workbenches.filter((wb) =>
    workshop.workbenchIds.includes(wb.id)
  );

  return (
    <div className="f-page">
      <Breadcrumb
        items={[
          { label: "Foundry", to: foundryHomePath() },
          { label: workshop.name }
        ]}
      />
      <header className="f-page-header">
        <h1 className="f-page-title">{workshop.name} Workshop</h1>
        <p className="f-page-subtitle">Select a workbench.</p>
      </header>
      <div className="f-grid f-grid--2">
        {workshopBenches.map((wb) => (
          <Link
            key={wb.id}
            to={workbenchHomePath(wb.id)}
            className="f-card f-card-link"
          >
            <h3>{wb.name}</h3>
            <p className="f-tech">{wb.slug}</p>
          </Link>
        ))}
        {workshopBenches.length === 0 ? (
          <div className="f-card">
            <h3>No workbenches yet</h3>
            <p>This workshop has no workbenches configured.</p>
          </div>
        ) : null}
      </div>
    </div>
  );
}
