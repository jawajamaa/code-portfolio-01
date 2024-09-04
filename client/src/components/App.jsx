import React, { useState } from 'react';
import CssBaseline from "@mui/material/CssBaseline";
import { Container } from "@mui/material";
import { Outlet } from "react-router-dom";
import fontTheme  from "../AppTheme";
import { createTheme } from "@mui/material/styles";
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

  return (
      <ThemeProvider theme={{darkTheme, fontTheme}}>
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
