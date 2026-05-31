import { Link } from "react-router-dom";
import type { ReactNode } from "react";
import "@/foundry-ui/theme/components.css";

export type BreadcrumbItem = {
  label: string;
  to?: string;
};

type BreadcrumbProps = {
  items: BreadcrumbItem[];
};

export function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <nav className="f-breadcrumb" aria-label="Breadcrumb">
      {items.map((item, index) => (
        <span key={`${item.label}-${index}`} className="f-breadcrumb-item">
          {item.to ? (
            <Link to={item.to} className="f-breadcrumb-link">
              {item.label}
            </Link>
          ) : (
            <span className="f-breadcrumb-current">{item.label}</span>
          )}
          {index < items.length - 1 ? (
            <span className="f-breadcrumb-sep" aria-hidden="true">
              {" "}
              &gt;{" "}
            </span>
          ) : null}
        </span>
      ))}
    </nav>
  );
}

type ConsolePageProps = {
  title: string;
  primaryQuestion: string;
  pattern: string;
  children: ReactNode;
  state?: "ready" | "empty" | "loading" | "error" | "blocked";
};

export function ConsolePage({
  title,
  primaryQuestion,
  pattern,
  children,
  state = "ready"
}: ConsolePageProps) {
  return (
    <article className="f-console-page">
      <header className="f-console-page-header">
        {pattern !== "landing" ? (
          <p className="f-console-pattern">
            Pattern: <span className="f-tech">{pattern}</span>
          </p>
        ) : null}
        <h2 className="f-console-title">{title}</h2>
        <p className="f-console-question">{primaryQuestion}</p>
      </header>
      <div className={`f-console-body f-console-body--${state}`}>{children}</div>
    </article>
  );
}
