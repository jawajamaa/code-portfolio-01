import React, { useState } from 'react';
import CssBaseline from "@mui/material/CssBaseline";
import { Container } from "@mui/material";
import { Outlet } from "react-router-dom";
import { createTheme } from "@mui/material/styles";
// import { darkTheme } from "../AppTheme";
// import { darkTheme, fontTheme } from "../AppTheme";
import { ThemeProvider } from "@mui/material/styles";
import { AppBarRenderProvider, useAppBarRender } from "../providers/AppBarRenderContext";

// import Home from './Home';
import RenderAppBarOrNot from "./styleNavMui/RenderAppBarOrNot";
import ResponsiveAppBar from "./styleNavMui/ResponsiveAppBar";
import './App.css';

function App() {
  const[toggleDarkMode, setToggleDarkMode] = useState(true);
  // const{ isAppBarRender } = useAppBarRender();

  const toggleDarkTheme = () => {
    setToggleDarkMode(!toggleDarkMode);
  };

  const darkTheme = createTheme({
      palette: {
        mode: toggleDarkMode ? 'dark' : 'light',
        primary: {
          main: '#212121'
        },
        secondary: {
          main: '#00e5ff'
        },
      },
  });

  // const darkTheme = createTheme({
  //     palette: {
  //       mode: toggleDarkMode ? 'dark' : 'light',
  //       primary: {
  //         main: '#1E1E1E'
  //       },
  //       secondary: {
  //         main: '#D9D9D9'
  //       },
  //     },
  // });

  // const combinedTheme = createTheme({
  //   ...darkTheme,
  //   // ...darkTheme(toggleDarkMode),
  //   ...fontTheme,
  // });

  console.log(toggleDarkMode ? "Dark Mode" : "Light Mode");
  // console.log(isAppBarRender ? "True" : "False");

  return (
      <ThemeProvider theme={darkTheme}>
      {/* <ThemeProvider theme={combinedTheme}> */}
        <AppBarRenderProvider>
          <Container>
            <header>
              <RenderAppBarOrNot>
                <ResponsiveAppBar 
                    toggleDarkMode = { toggleDarkMode }
                    toggleDarkTheme = { toggleDarkTheme }
                  />
              </RenderAppBarOrNot>
            </header>
            <main>
              <Outlet />
              <CssBaseline />
            </main>
          </Container>
        </AppBarRenderProvider>
    </ThemeProvider>
  );
}

export default App
