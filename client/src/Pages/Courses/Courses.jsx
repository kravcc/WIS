import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { LoggedUserContext } from "../../Context/LoggedUser";
import ManageAllCourses from "./ManageAllCourses/ManageAllCourses";


const Courses = () => {
    const {loggedUser, setLoggedUser} = useContext(LoggedUserContext)
    const [isLoggedIn, setIsLoggedIn] = useState(!!loggedUser.token)

    const navigate = useNavigate();

    useEffect(() => {
        if (!loggedUser.role) navigate('/login')
    }, [loggedUser])

    if (loggedUser.role === 'a')
    return (<ManageAllCourses/>)
}

export default Courses