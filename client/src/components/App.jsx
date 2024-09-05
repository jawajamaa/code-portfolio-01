import React, { useState } from 'react';
import CssBaseline from "@mui/material/CssBaseline";
import { Container } from "@mui/material";
import { Outlet } from "react-router-dom";
import { createTheme } from "@mui/material/styles";
import { darkTheme, fontTheme } from "../AppTheme";
import { ThemeProvider } from "@mui/material/styles";

// import Home from './Home';
import ResponsiveAppBar from "./styleNavMui/ResponsiveAppBar";
import './App.css';

function App() {
  const[ toggleDarkMode, setToggleDarkMode ] = useState(true);

  const toggleDarkTheme = () => {
    setToggleDarkMode(!toggleDarkMode);
  };

  const combinedTheme = createTheme({
    ...darkTheme(toggleDarkMode),
    ...fontTheme,
  });

  console.log(toggleDarkMode ? "Dark Mode" : "Light Mode");
  
  return (
      <ThemeProvider theme={combinedTheme}>
        <Container>
          <header>
             <ResponsiveAppBar 
                toggleDarkMode = { toggleDarkMode }
                toggleDarkTheme = { toggleDarkTheme }
              />
          </header>
          <main>
            <CssBaseline />
            <Outlet />
          </main>
        </Container>
    </ThemeProvider>
  );
}

export default App
