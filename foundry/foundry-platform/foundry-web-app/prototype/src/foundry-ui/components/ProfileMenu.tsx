import * as DropdownMenu from "@radix-ui/react-dropdown-menu";
import { currentUser } from "@/lib/data";
import "@/foundry-ui/theme/components.css";

function getInitials(name: string): string {
  return name
    .split(" ")
    .map((part) => part[0] ?? "")
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

export function ProfileMenu() {
  const initials = getInitials(currentUser.name);

  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        <button
          type="button"
          className="f-profile-trigger"
          aria-label={`Open profile menu for ${currentUser.name}`}
        >
          {currentUser.avatarUrl ? (
            <img
              src={currentUser.avatarUrl}
              alt=""
              className="f-profile-avatar"
            />
          ) : (
            <span className="f-profile-avatar f-profile-avatar--initials" aria-hidden="true">
              {initials}
            </span>
          )}
          <span className="f-profile-name">{currentUser.name}</span>
        </button>
      </DropdownMenu.Trigger>
      <DropdownMenu.Portal>
        <DropdownMenu.Content
          className="f-profile-menu"
          sideOffset={6}
          align="end"
        >
          <div className="f-profile-menu-header">
            <span className="f-profile-menu-name">{currentUser.name}</span>
            <span className="f-profile-menu-email">{currentUser.email}</span>
          </div>
          <DropdownMenu.Separator className="f-profile-menu-separator" />
          <DropdownMenu.Item className="f-profile-menu-item">
            View profile
          </DropdownMenu.Item>
          <DropdownMenu.Item className="f-profile-menu-item">
            Preferences
          </DropdownMenu.Item>
          <DropdownMenu.Separator className="f-profile-menu-separator" />
          <DropdownMenu.Item className="f-profile-menu-item f-profile-menu-item--danger">
            Sign out
          </DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}
