import { Button, Container, Stack } from "@chakra-ui/react"
import Navbar from "./components/Navbar"

function App() {
  return (
    <Stack minH={"100vh"}>
       <Navbar></Navbar>

       <Container maxW={"1200px"} my={4}></Container>
    </Stack>
  )
}

export default App
