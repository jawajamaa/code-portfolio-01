import * as React from 'react';
import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';
// import DeleteIcon from '@mui/icons-material/Delete';
// import SendIcon from '@mui/icons-material/Send';
// import Stack from '@mui/material/Stack';

export default function IconLabelButton() {
  return (
      <Button variant="contained" endIcon={<DownloadIcon />}>
        Send
      </Button>
  );
}
