import * as Dialog from "@radix-ui/react-dialog";
import type { ReactNode } from "react";
import { Button } from "@/foundry-ui/components/Button";
import "@/foundry-ui/theme/components.css";

type FoundryDialogProps = {
  title: string;
  description: string;
  triggerLabel: string;
  children: ReactNode;
};

export function FoundryDialog({
  title,
  description,
  triggerLabel,
  children
}: FoundryDialogProps) {
  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <Button variant="secondary">{triggerLabel}</Button>
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="f-dialog-overlay" />
        <Dialog.Content className="f-dialog-content">
          <Dialog.Title className="f-dialog-title">{title}</Dialog.Title>
          <Dialog.Description className="f-dialog-description">
            {description}
          </Dialog.Description>
          <div>{children}</div>
          <div className="f-dialog-actions">
            <Dialog.Close asChild>
              <Button variant="ghost">Close</Button>
            </Dialog.Close>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
