import { Button, StatusBadge } from "@/foundry-ui/components";

export function BuildView() {
  return (
    <section className="f-grid">
      <div className="f-card">
        <h3>Build Console</h3>
        <p>
          Storyline coverage: Product Intent stage transitions, Work Orders, and
          governance visibility.
        </p>
      </div>

      <div className="f-grid f-grid--2">
        <div className="f-card">
          <h3>Product Intent PI-188</h3>
          <p>
            Current stage: <span className="f-tech">implementation-ready</span>
          </p>
          <div style={{ marginTop: "0.75rem", display: "flex", gap: "0.5rem" }}>
            <StatusBadge tone="success">On Track</StatusBadge>
            <StatusBadge tone="governance-pass">Gate Passed</StatusBadge>
          </div>
        </div>
        <div className="f-card">
          <h3>Work Order Queue</h3>
          <p>
            <span className="f-tech">WO-517</span> Spec finalization
          </p>
          <p>
            <span className="f-tech">WO-518</span> QA plan prep (parallel branch)
          </p>
          <div style={{ marginTop: "0.75rem" }}>
            <Button variant="secondary">View Work Orders</Button>
          </div>
        </div>
      </div>
    </section>
  );
}
