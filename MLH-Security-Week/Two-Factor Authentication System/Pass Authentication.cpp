#include <iostream>
#include <string>

bool verifyOTP(const std::string& enteredOTP)
{
    // Simulated OTP for demonstration purposes
    const std::string storedOTP = "123456";

    return enteredOTP == storedOTP;
}

int main()
{
    std::string username;
    std::string password;
    std::string otp;

    std::cout << "Enter your username: ";
    std::cin >> username;

    std::cout << "Enter your password: ";
    std::cin >> password;

    std::cout << "Enter the OTP: ";
    std::cin >> otp;

    bool isAuthenticated = verifyOTP(otp);

    if (isAuthenticated)
    {
        std::cout << "Authentication successful!" << std::endl;
    }
    else
    {
        std::cout << "Authentication failed!" << std::endl;
    }

    return 0;
}
