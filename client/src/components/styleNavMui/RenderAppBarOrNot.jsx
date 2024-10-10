import React, {useEffect, useState} from "react";
import {useLocation} from "react-router-dom";

function RenderAppBarOrNot({ children }) {
    const[noAppBar, setNoAppBar] = useState(false);
    const location = useLocation();

    useEffect(() => {
        console.log("This is location", location)
        if(location.pathname === "/" || location.pathname === "/aboutme"){
            setNoAppBar(false)
        } else {
            setNoAppBar(true)
        }
    },[location])

    return(
        <div>
            {noAppBar && children}
        </div>
    )
}

export default RenderAppBarOrNot;
