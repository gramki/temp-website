import { useState } from "react";
import { BuildView } from "@/features/build/BuildView";
import { DiscoveryView } from "@/features/discovery/DiscoveryView";
import { AppShell, FoundryTabs } from "@/foundry-ui/components";

export function App() {
  const [tab, setTab] = useState("discovery");

  return (
    <AppShell
      breadcrumb="Foundry > Workshop Helios > Workbench Orion > Prototype"
      title="Foundry Web App Prototype"
    >
      <FoundryTabs
        value={tab}
        onValueChange={setTab}
        tabs={[
          { value: "discovery", label: "Discovery Track" },
          { value: "build", label: "Build Track" }
        ]}
      />
      {tab === "discovery" ? <DiscoveryView /> : <BuildView />}
    </AppShell>
  );
}
