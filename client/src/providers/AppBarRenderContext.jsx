import { createContext, useContext, useState } from "react";

const AppBarRenderContext = createContext();

export function AppBarRenderProvider({ children }) {
    const [isAppBarRender, setIsAppBarRender] = useState(true);

    return(
        <AppBarRenderContext.Provider value = {{ isAppBarRender, setIsAppBarRender }}>
            { children }
        </AppBarRenderContext.Provider>
    );
}

export function useAppBarRender() {
    return useContext(AppBarRenderContext);
}
