//
//  HomeViewModel.swift
//  Mood
//
//  Created by Hascats on 2021/6/19.
//

import Foundation
import Combine

class HomeViewModel: ObservableObject {
    func logoutUser() {
        UserDefaults.standard.removeObject(forKey: "token")
        AppManager.Authenticated.send(false)
    }
}
