import { createContext, useContext, useState } from "react";

const UrlContext = createContext();

export function UrlProvider({ children }) {
    const [baseUrl, setBaseUrl] = useState("http://localhost:5555");
    const [myGhUrl, setMyGhUrl] = useState("https://github.com/jawajamaa");
    const [myLinkedIn, setMyLinkedIn] = useState("https://www.linkedin.com/in/timothy-ryon/");

    return(
        <UrlContext.Provider value = {{ baseUrl, setBaseUrl, myGhUrl, setMyGhUrl, myLinkedIn, setMyLinkedIn }}>
            { children }
        </UrlContext.Provider>
    );
}

export function useUrl() {
    return useContext(UrlContext);
}
