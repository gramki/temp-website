import { Button, FoundryDialog, StatusBadge } from "@/foundry-ui/components";

export function DiscoveryView() {
  return (
    <section className="f-grid">
      <div className="f-card">
        <h3>Discovery Console</h3>
        <p>
          Storyline coverage: create case, stage progression, and decision gate to
          proceed-to-build.
        </p>
      </div>
      <div className="f-grid f-grid--2">
        <div className="f-card">
          <h3>Discovery Case DC-241</h3>
          <p>
            Owner: Product Manager <span className="f-tech">pm-anika</span>
          </p>
          <div style={{ marginTop: "0.75rem", display: "flex", gap: "0.5rem" }}>
            <StatusBadge tone="info">Research Active</StatusBadge>
            <StatusBadge tone="governance-review">Review Required</StatusBadge>
          </div>
        </div>
        <div className="f-card">
          <h3>Actions</h3>
          <div style={{ display: "flex", gap: "0.5rem", marginTop: "0.75rem" }}>
            <Button>Advance Stage</Button>
            <FoundryDialog
              triggerLabel="Open Decision Gate"
              title="Proceed to Build"
              description="Decision gate captures rationale and creates Product Intent handoff."
            >
              <StatusBadge tone="governance-soft-block">
                Missing UX evidence
              </StatusBadge>
            </FoundryDialog>
          </div>
        </div>
      </div>
    </section>
  );
}
