import { useUrl } from "../providers/UrlContext";
import { NavLink } from "react-router-dom";

import { Box, Grid2, Typography } from "@mui/material";
import GitHubIcon from "@mui/icons-material/GitHub";
import LinkedInIcon from "@mui/icons-material/LinkedIn";

import Item from "./Item";
import "./BannerMe.css";

function BannerMe(){
    const { myGhUrl, myLinkedIn } = useUrl();

    return(
        <Grid2 size={12}>
        <Item>
            <Grid2 
                container spacing={2}
                display="flex"
                alignItems="center"
            >
                <Grid2 size={{ xs: 6, md: 2 }} offset={{ xs: 3, md: 0 }}>
                    <a href = { myGhUrl }
                        target = "_blank"
                        className={"link"}>
                    <GitHubIcon />
                    </a>
                </Grid2>
                <Grid2 size={{ xs: 'grow', md: 4 }} offset={{ md: 2 }}>
                    <nav id = "nameLink">
                        <NavLink to = {'/'}>
                            <Typography>timothy ryon</Typography>
                            <Typography>Developer</Typography>
                        </NavLink>
                    </nav>
                </Grid2>
                <Grid2 size={{ xs: 4, md: 2 }} offset={{ md: 'auto' }}>
                    <a href = { myLinkedIn }
                        target = "_blank"
                        className = {"link"}>
                        <LinkedInIcon />
                    </a>
                </Grid2>
            </Grid2>
        </Item>
    </Grid2>
    )
};

export default BannerMe;
