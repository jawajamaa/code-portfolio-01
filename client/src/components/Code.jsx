import { Box, Grid2, Typography } from "@mui/material";
import DownloadIcon from '@mui/icons-material/Download';

import IconLabelButton from "./styleNavMui/IconLabelButton";
import resume from "../../public/documents/Ryon-Timothy_Resume.pdf";

// rename or remake section to 'A little more about me'.  Keep the resume download, but perhaps put a little more fun information here, and keep the splash/home page short and succinct and more 'professional'? And can add the quad-tich fun photos?  Maybe move the aperture logo and link here?  Again, keeping the splash page simple and extras here for anyone who takes the extra time to look further.
function Code() {
    
    return(
        <Box sx={{ flexGrow:1 }}>
            <Grid2 container spacing={2}>
                <Grid2 size={12}>
                    <Typography>01100011 01101111 01100100 01100101 </Typography>
                </Grid2>
                <Grid2 size={12}>
                    <a href={resume} download="Ryon-Timothy_Resume">
                        <IconLabelButton 
                            icon={<DownloadIcon />}
                            label="Download Resume"/>
                    </a>
                </Grid2>
            </Grid2>
        </Box>
    );
}

export default Code;
