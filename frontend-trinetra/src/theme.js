 import {createContext,useState,useMemo} from "react";
 import { createTheme } from "@mui/material";


//Color code 
// #E5E6E5 //platinum white
// #2E2E2E // jet black
// #91E76C //lightgreen
// #D4E232// oear yellowgreen pear
// #26FFE6 // skyblue fluorescent cyan

export const tokens=(mode)=>({
    ...(mode ==='dark'
    ?{
        whiteAccent: {
            100: "#fafafa",
            200: "#f5f5f5",
            300: "#eff0ef",
            400: "#eaebea",
            500: "#e5e6e5",
            600: "#b7b8b7",
            700: "#898a89",
            800: "#5c5c5c",
            900: "#2e2e2e"
        },
        primary: {
            100: "#d5d5d5",
            200: "#ababab",
            300: "#828282",
            400: "#585858",
            500: "#2e2e2e",
            600: "#252525",
            700: "#1c1c1c",
            800: "#121212",
            900: "#090909"
        },
        greenAccent: {
            100: "#e9fae2",
            200: "#d3f5c4",
            300: "#bdf1a7",
            400: "#a7ec89",
            500: "#91e76c",
            600: "#74b956",
            700: "#578b41",
            800: "#3a5c2b",
            900: "#1d2e16"
        },
        yellowAccent: {
            100: "#f6f9d6",
            200: "#eef3ad",
            300: "#e5ee84",
            400: "#dde85b",
            500: "#d4e232",
            600: "#aab528",
            700: "#7f881e",
            800: "#555a14",
            900: "#2a2d0a"
        },
        blueAccent: {
            100: "#d4fffa",
            200: "#a8fff5",
            300: "#7dfff0",
            400: "#51ffeb",
            500: "#26ffe6",
            600: "#1eccb8",
            700: "#17998a",
            800: "#0f665c",
            900: "#08332e"
        },

    }:
    {

        whiteAccent: {
            100: "#2e2e2e",
            200: "#5c5c5c",
            300: "#898a89",
            400: "#b7b8b7",
            500: "#e5e6e5",
            600: "#eaebea",
            700: "#eff0ef",
            800: "#f5f5f5",
            900: "#fafafa",
        },
        primary: {
            100: "#090909",
            200: "#121212",
            300: "#1c1c1c",
            400: "#252525",
            500: "#2e2e2e",
            600: "#585858",
            700: "#828282",
            800: "#ababab",
            900: "#d5d5d5",
        },
        greenAccent: {
            100: "#1d2e16",
            200: "#3a5c2b",
            300: "#578b41",
            400: "#74b956",
            500: "#91e76c",
            600: "#a7ec89",
            700: "#bdf1a7",
            800: "#d3f5c4",
            900: "#e9fae2",
        },
        yellowAccent: {
            100: "#2a2d0a",
            200: "#555a14",
            300: "#7f881e",
            400: "#aab528",
            500: "#d4e232",
            600: "#dde85b",
            700: "#e5ee84",
            800: "#eef3ad",
            900: "#f6f9d6",
        },
        blueAccent: {
            100: "#08332e",
            200: "#0f665c",
            300: "#17998a",
            400: "#1eccb8",
            500: "#26ffe6",
            600: "#51ffeb",
            700: "#7dfff0",
            800: "#a8fff5",
            900: "#d4fffa",
        },



    }),


});

export const themeSettings=(mode)=>{
    const colors=tokens(mode);

    return{
        palette:{
            mode:mode,
            ...(mode === 'dark')
        ?{
            primary:{
                main:colors.primary[500]
            },
            secondary:{
                main:colors.greenAccent[500]
            },
            neutral:{
                dark:colors.yellowAccent[700],
                main:colors.yellowAccent[500],
                light:colors.yellowAccent[100]
            },
            background:{
                default:colors.primary[500]
            }

        }
        :{
            primary:{
                main:colors.whiteAccent[500]
            },
            secondary:{
                main:colors.primary[500]
            },
            neutral:{
                dark:colors.blueAccent[700],
                main:colors.blueAccent[500],
                light:colors.blueAccent[100]
            },
            background:{
                default:colors.whiteAccent[500]
            }

        }
    },
    typography: {
        fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
        fontSize: 12,
        h1: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 40,
        },
        h2: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 32,
        },
        h3: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 24,
        },
        h4: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 20,
        },
        h5: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 16,
        },
        h6: {
          fontFamily: ["Source Sans Pro", "sans-serif"].join(","),
          fontSize: 14,
        },
      },
    };
  };
  
  // context for color mode
  export const ColorModeContext = createContext({
    toggleColorMode: () => {},
  });
  
  export const useMode = () => {
    const [mode, setMode] = useState("dark");
  
    const colorMode = useMemo(
      () => ({
        toggleColorMode: () =>
          setMode((prev) => (prev === "light" ? "dark" : "light")),
      }),
      []
    );
  
    const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);
    return [theme, colorMode];
  };