import * as RadixTabs from "@radix-ui/react-tabs";
import { cn } from "@/lib/cn";
import "@/foundry-ui/theme/components.css";

type FoundryTabsProps = {
  value: string;
  onValueChange: (value: string) => void;
  tabs: Array<{ value: string; label: string }>;
};

export function FoundryTabs({ value, onValueChange, tabs }: FoundryTabsProps) {
  return (
    <RadixTabs.Root value={value} onValueChange={onValueChange}>
      <RadixTabs.List className="f-tabs-list" aria-label="Journey tabs">
        {tabs.map((tab) => (
          <RadixTabs.Trigger
            key={tab.value}
            value={tab.value}
            className={cn("f-tab-trigger")}
          >
            {tab.label}
          </RadixTabs.Trigger>
        ))}
      </RadixTabs.List>
    </RadixTabs.Root>
  );
}
