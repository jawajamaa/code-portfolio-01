import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import routes from './AppRoutes';

import CssBaseLine from "@mui/material/CssBaseLine";
import { ThemeProvider } from "@mui/material/styles";

import App from "./components/App";
import theme from "./AppTheme";
import "./index.css";

const router = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <ThemeProvider theme={theme}>
        <CssBaseLine />
        <RouterProvider router = { router } />
    </ThemeProvider>
);
