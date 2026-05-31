import { cn } from "@/lib/cn";
import "@/foundry-ui/theme/components.css";

export type BadgeTone =
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

type StatusBadgeProps = {
  tone: BadgeTone;
  children: string;
  className?: string;
};

export function StatusBadge({ tone, children, className }: StatusBadgeProps) {
  return (
    <span className={cn("f-badge", `f-badge--${tone}`, className)}>{children}</span>
  );
}
