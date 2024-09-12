import React, { useState } from 'react';
import CssBaseline from "@mui/material/CssBaseline";
import { Container } from "@mui/material";
import { Outlet } from "react-router-dom";
import { createTheme } from "@mui/material/styles";
// import { darkTheme } from "../AppTheme";
// import { darkTheme, fontTheme } from "../AppTheme";
import { ThemeProvider } from "@mui/material/styles";

// import Home from './Home';
import ResponsiveAppBar from "./styleNavMui/ResponsiveAppBar";
import './App.css';

function App() {
  const[ toggleDarkMode, setToggleDarkMode ] = useState(true);

  const toggleDarkTheme = () => {
    setToggleDarkMode(!toggleDarkMode);
  };

  const darkTheme = createTheme({
      palette: {
        mode: toggleDarkMode ? 'dark' : 'light',
        primary: {
          main: '#1E1E1E'
        },
        secondary: {
          main: '#D9D9D9'
        },
      },
  });

  // const combinedTheme = createTheme({
  //   ...darkTheme,
  //   // ...darkTheme(toggleDarkMode),
  //   ...fontTheme,
  // });

  console.log(toggleDarkMode ? "Dark Mode" : "Light Mode");
  // console.log(combinedTheme);

  return (
      <ThemeProvider theme={darkTheme}>
      {/* <ThemeProvider theme={combinedTheme}> */}
        <Container>
          <header>
             <ResponsiveAppBar 
                toggleDarkMode = { toggleDarkMode }
                toggleDarkTheme = { toggleDarkTheme }
              />
          </header>
          <main>
            <Outlet />
            <CssBaseline />
          </main>
        </Container>
    </ThemeProvider>
  );
}

export default App
