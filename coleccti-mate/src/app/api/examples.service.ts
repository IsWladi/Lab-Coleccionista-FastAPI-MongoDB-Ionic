import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class ExamplesService {
  constructor() {}
  apiUrl = environment.apiUrl;
  async getAllUsersWithoutAuth(): Promise<any> {
    // Make a request for a user with a given ID
    axios
      .get(this.apiUrl + 'api/examples/get/all/users/without/authentication')
      .then(function (response) {
        // handle success
        console.log(response.data[0]);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
  }
}

