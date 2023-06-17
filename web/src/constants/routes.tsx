import { RouteObject, createBrowserRouter } from "react-router-dom";
import Home from "../screens/Home";

const routes: RouteObject[] = [
  {
    path: "/*",
    element: <Home />,
  },
];

const router = createBrowserRouter(routes);
export default router;
