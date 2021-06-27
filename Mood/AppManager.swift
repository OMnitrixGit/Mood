//
//  AppManager.swift
//  Mood
//
//  Created by Hascats on 2021/6/19.
//

import Foundation
import Combine

struct AppManager {
    
    static let Authenticated = PassthroughSubject<Bool, Never>()
    
    static func IsAuthenticated() -> Bool {
        return UserDefaults.standard.string(forKey: "token") != nil
    }
}
