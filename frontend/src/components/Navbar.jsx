import { Box, Center, Container, Flex, Text } from '@chakra-ui/react'

const Navbar = () => {
  return (
    <Container maxW={"900px"}>
      <Box px={4} my={4} borderRadius={5} bg={"gray.700"}>
        <Flex h={16} alignItems={"center"} justifyContent={"space-between"}>
          {/* Left side */}
        <Flex alignItems={"center"} justifyContent={"center"} gap={3} display={{base:"none", sm:"flex"}}>
          <img src="/react.png" alt="react logo" width={50} height={50} />
          <Text fontSize={"40px"}>+</Text>
          <img src="/python.png" alt="pythom logo" width={50} height={40} />
          <Text fontSize={"40px"}>=</Text>
          <img src="/explode.png" alt="explode logo" width={45} height={45} />
        </Flex>
          {/* Left side */}
          {/* Right side */}
        <Flex></Flex>
          {/* Right side */}
        </Flex>
      </Box>
      Navbar
      </Container> 
  )
}

export default Navbar