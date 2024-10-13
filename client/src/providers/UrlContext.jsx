import { createContext, useContext, useState } from "react";

const UrlContext = createContext();

export function UrlProvider({ children }) {
    const [baseUrl, setBaseUrl] = useState("http://localhost:5555");
    const [imageUrl, setImageUrl] = useState("/imagefiles");
    const [aboutMeUrl, setAboutMeUrl] = useState("/aboutmefiles");
    const [myGhUrl, setMyGhUrl] = useState("https://github.com/jawajamaa");
    const [myLinkedIn, setMyLinkedIn] = useState("https://www.linkedin.com/in/timothy-ryon/");
    const [myRecipeLoom, setMyRecipeLoom] = useState("https://www.loom.com/share/6142869e598443269dee45247855a43a?sid=b2d9b9a6-05f3-42d0-8866-f2e3051580a4")
    const [myDigiWallpaperLoom, setMyDigiWallpaperLoom] = useState("https://www.loom.com/share/6142869e598443269dee45247855a43a?sid=b2d9b9a6-05f3-42d0-8866-f2e3051580a4")
// ////////////////////////////////////////////////////////////////////////
// NOTE: remove unneccessary setter functions from provider when finished and is actually not needed?

    return(
        <UrlContext.Provider value = {{ aboutMeUrl, setAboutMeUrl, baseUrl, setBaseUrl, imageUrl, setImageUrl, myGhUrl, setMyGhUrl, myLinkedIn, setMyLinkedIn, myDigiWallpaperLoom, setMyDigiWallpaperLoom, myRecipeLoom, setMyRecipeLoom }}>
            { children }
        </UrlContext.Provider>
    );
}

export function useUrl() {
    return useContext(UrlContext);
}
