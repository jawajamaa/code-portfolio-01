import { createTheme } from "@mui/material/styles";
import PlayfairDisplay from "./Fonts/PlayfairDisplay-VariableFont_wght.ttf";

const playfairDisplay = {
    fontFamily: "PlayfairDisplay",
    fontStyle: "normal",
    fontDisplay: "swap",
    fontWeight: "600",
    src: `
        local("PlayfairDisplay"),
        local("PlayfairDisplay-Normal"),
        url(${PlayfairDisplay}) format("ttf")
        `,
    unicodeRange:
        "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF",
};

const fontTheme = createTheme({
    typography: {
        fontfamily: ['"Open Sans"', "PlayfairDisplay", "Roboto"].join(","),
    },
    overrides: {
        MuiCssBaseline: {
            "@global": {
                "@font-face": [playfairDisplay],
            },
        }
    }
});

// export default fontTheme;

  // applying the primary and secondary theme colors
  const darkTheme = (toggleDarkMode) => 
    createTheme({
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


export { darkTheme, fontTheme };
