/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/12 23:08:26 by yhetman           #+#    #+#             */
/*   Updated: 2019/11/12 23:37:34 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	dihotomia(double eps, double a, double b);
void	mod_Newton(double eps, double a, double b);

int main(void)
{
	double eps, a, b;

	eps = 10 ^ (-4);
	a = 0;
	b = M_PI / 2;
	dihotomia(eps, a, b);
	mod_Newton(eps, a, b);
	return (0);
}
