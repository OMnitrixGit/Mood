//
//  LoginViewModel.swift
//  Mood
//
//  Created by Hascats on 2021/6/19.
//

import SwiftUI
import Combine

class LoginViewModel: ObservableObject {
    @Published var email = ""
    @Published var password = ""
    
    var errorMessage = ""
}

extension LoginViewModel {
    func loginUser() -> Bool {
        if email == "dev@dev.com",
           password == "12341234" {
            let token = UUID().uuidString
            UserDefaults.standard.set(token, forKey: "token")
            AppManager.Authenticated.send(true)
            
            return true
        } else {
            errorMessage = "Invalid credentials"
            return false
        }
    }
}
