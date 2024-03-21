import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class ExamplesService {
  constructor() {}
  apiUrl = environment.apiUrl;
  userToken = "";
  async login(username: string, password: string) {
    try{
      const form = new FormData();
      form.append('username', username);
      form.append('password', password);
      const response = await axios.post(this.apiUrl + 'api/auth/token', form)
      this.userToken = response.data.access_token
    }catch(e){
      console.log(e)
    }

  }
  async getAllUsersWithoutAuth() {
    try{
      const response = await axios.get(this.apiUrl + 'api/examples/get/all/users/without/authentication')
      console.log(response.data);
    }
    catch(e){
      console.log(e)
    }
  }


  async getAllUsersWithAuth() {
    try{
      const bearerToken = 'Bearer ' + this.userToken;
      const response = await axios.get(this.apiUrl + 'api/examples/get/all/users/with/required/authentication', {
        headers: {
          'Authorization': bearerToken
        }
      })
      console.log(response.data);
    }
    catch(e){
      console.log(e)
    }
  }


}

