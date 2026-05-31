import type { ReactNode } from "react";
import "@/foundry-ui/theme/components.css";

type AppShellProps = {
  title: string;
  breadcrumb: string;
  children: ReactNode;
};

export function AppShell({ title, breadcrumb, children }: AppShellProps) {
  return (
    <div className="f-shell">
      <header className="f-shell-header">
        <p className="f-shell-breadcrumb">{breadcrumb}</p>
        <h1 className="f-shell-title">{title}</h1>
      </header>
      <main className="f-shell-main">{children}</main>
    </div>
  );
}
