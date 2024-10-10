import Airport from "./components/Airport";
import AirportOverlay from "./components/AirportOverlay";
import App from "./components/App";
import Code from "./components/AboutMe";
import ErrorPage from "./components/ErrorPage";
import FromTheHip from "./components/FromTheHip";
import FromTheHipOverlay from "./components/FromTheHipOverlay";
import Home from "./components/Home";
import PhotographyMain from "./components/PhotographyMain";
import Place from "./components/Place";
import PlaceOverlay from "./components/PlaceOverlay";
import Space from "./components/Space";
import SpaceOverlay from "./components/SpaceOverlay";


const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/aboutme",
                element: <Code />
            },
            {
                path: "/photography",
                element: <PhotographyMain />,
            },
            {
                path: "/photography/space",
                element: <Space />
            },
            {
                path: "/photography/space/:id",
                element: <SpaceOverlay />
                // or just one Overlay component?Possibly not..
            },
            {
                path: "/photography/place",
                element: <Place />
            },
            {
                path: "/photography/place/:id",
                element: <PlaceOverlay />
            },
            {
                path: "/photography/airport",
                element: <Airport />
            },
            {
                path: "/photography/airport/:id",
                element: <AirportOverlay />
            },
            {
                path: "/photography/from-the-hip",
                element: <FromTheHip />
            },
            {
                path: "/photography/from-the-hip/:id",
                element: <FromTheHipOverlay />
            },
        ]
    }
];

export default routes;
