import { Navigate, Route, Routes } from "react-router-dom";
import { FoundryTopBar } from "@/foundry-ui/components/FoundryTopBar";
import { FoundryHome } from "@/features/home/FoundryHome";
import { WorkshopHome } from "@/features/home/WorkshopHome";
import { WorkbenchWall } from "@/features/home/WorkbenchWall";
import {
  ConsoleContent,
  OrchestrationItemDetail,
  TeamMemberDetail,
  WorkspaceSessionDetail
} from "@/features/consoles/ConsoleContent";
import { WorkOrderDetail } from "@/features/workorders/WorkOrderDetail";
import { WorkbenchShell } from "@/foundry-ui/components/WorkbenchShell";
import { DEFAULT_WORKBENCH_ID, workbenchHomePath } from "@/lib/routes";
import "@/foundry-ui/theme/components.css";

export function App() {
  return (
    <div className="f-app">
      <FoundryTopBar />
      <div className="f-app-content">
        <Routes>
          <Route path="/" element={<FoundryHome />} />
          <Route path="/workshops/:workshopId" element={<WorkshopHome />} />
          <Route path="/workbenches/:workbenchId" element={<WorkbenchShell />}>
            <Route index element={<WorkbenchWall />} />
            <Route path="consoles/:consoleId" element={<ConsoleContent />} />
          </Route>
          <Route
            path="/workbenches/:workbenchId/orchestration/:type/:itemId"
            element={<OrchestrationItemDetail />}
          />
          <Route
            path="/workbenches/:workbenchId/team/:memberId"
            element={<TeamMemberDetail />}
          />
          <Route
            path="/workbenches/:workbenchId/sessions/:sessionId"
            element={<WorkspaceSessionDetail />}
          />
          <Route
            path="/workbenches/:workbenchId/work-orders/:workOrderId"
            element={<WorkOrderDetail />}
          />
          <Route
            path="*"
            element={
              <Navigate to={workbenchHomePath(DEFAULT_WORKBENCH_ID)} replace />
            }
          />
        </Routes>
      </div>
    </div>
  );
}
