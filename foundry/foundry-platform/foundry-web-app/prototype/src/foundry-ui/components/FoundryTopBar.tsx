import { Link } from "react-router-dom";
import { tenant } from "@/lib/data";
import { foundryHomePath } from "@/lib/routes";
import { ProfileMenu } from "./ProfileMenu";
import "@/foundry-ui/theme/components.css";

export function FoundryTopBar() {
  return (
    <header className="f-top-bar">
      <Link to={foundryHomePath()} className="f-top-bar-title">
        {tenant.name} Foundry
      </Link>
      <ProfileMenu />
    </header>
  );
}
