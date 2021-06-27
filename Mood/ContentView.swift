//
//  ContentView.swift
//  Mood
//
//  Created by Hascats on 2021/6/18.
//

import SwiftUI
struct Result:Codable{
    let id : Int
    let labels: String
    let url : String
}

struct Response:Codable{
    
    let results : [Result]
}


struct ContentView: View {
    
    @State var isAuthenticated = AppManager.IsAuthenticated()
    @State var results : [Result] = []

    
    
    var body: some View {
        TabView{
            NavigationView{
                ScrollView(.vertical){
                    ForEach(self.results,id:\.id){ item in
                        LazyVStack{
                            URLImage(withURL: item.url)
                            HStack{
                                Text(item.labels)
                            }.frame(width: 300, height: 40, alignment: /*@START_MENU_TOKEN@*/.center/*@END_MENU_TOKEN@*/)
                            .background(Color.gray)
                            
                        }
                    }
                }.navigationBarTitle(Text("Mood"))
            }
            .tabItem {
                Image(systemName: "photo.on.rectangle")
                Text("Mood")
            }
            
            
            
            Group {
                isAuthenticated ? AnyView(HomeView()) : AnyView(LoginView())
            }
            .onReceive(AppManager.Authenticated, perform: {
                isAuthenticated = $0
            }).tabItem {
                Image(systemName: "person.crop.circle")
                Text("Login")
            }
        }
        .onAppear(perform: request_data)

    }
    
    func request_data(){
        guard let url = URL(string:"https://www.hascats.cn")
            else { return }
            URLSession.shared.dataTask(with: url){ (data,response,error) in
                guard let data = data,
                      let decodedData = try? JSONDecoder().decode(Response.self,from: data)
                else { return }
                
                self.results = decodedData.results
                
            }.resume()
    }

}
 









struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
