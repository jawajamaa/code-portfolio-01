import React, { useEffect } from "react";
import { Container } from "@mui/material";

import { useAppBarRender } from "../providers/AppBarRenderContext";

function Home(){
    const{ isAppBarRender, setIsAppBarRender } = useAppBarRender();

    // useEffect()

    return(
        <Container>
            <h1>There's no Place Like /</h1>
            <div>
                <h2>01100011 01101111 01100100 01100101 </h2>
                <h2>Photography</h2>
            </div>
        </Container>
    );
}

export default Home;
