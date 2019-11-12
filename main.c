/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/12 23:08:26 by yhetman           #+#    #+#             */
/*   Updated: 2019/11/12 23:12:03 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	dihotomia(double eps, double a, double b);

int main()
{
	double eps, a, b;

	eps = 10 ^ (-4);
	a = 0;
	b = 3.1415 / 2;
	dihotomia(eps, a, b);
	return (0);
}
