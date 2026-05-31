import type { ButtonHTMLAttributes } from "react";
import { cn } from "@/lib/cn";
import "@/foundry-ui/theme/components.css";

type ButtonVariant = "primary" | "secondary" | "critical" | "ghost";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant;
};

export function Button({
  className,
  variant = "primary",
  type = "button",
  ...props
}: ButtonProps) {
  return (
    <button
      type={type}
      className={cn("f-button", `f-button--${variant}`, className)}
      {...props}
    />
  );
}
