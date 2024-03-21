import { Component, OnInit } from '@angular/core';
import { ExamplesService } from '../api/examples.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
})
export class Tab1Page implements OnInit {
  constructor(private apiService: ExamplesService) {
  }

  async ngOnInit() {
    await this.apiService.login("wladi1", "duoc123456");
    if( this.apiService.userToken != ""){
      console.log("Login success")
      console.log("user token: " + this.apiService.userToken)
    }
    else{
      console.log("invalid credentials (Unauthorized)")
    }
    console.log("Getting all users without authentication")
    await this.apiService.getAllUsersWithoutAuth();
    console.log("Getting all users with authentication (using token)")
    await this.apiService.getAllUsersWithAuth();
  }
  //
}
